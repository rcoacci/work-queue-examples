################################################################################
#
# This example shows how to execute native python functions as Work Queue
# tasks. In particular, the python function 'application_function(x,y)' (which
# simply computes y/x) is executed remotely at workers as Work Queue task for
# various combinations of arguments.
#
# A Work Queue task is created by writing the desired function and its
# arguments to a file (i.e., serialization). At the worker, these files are
# read and the function call is executed. The output of the function is then
# serialized and sent back to the Work Queue manager, where it is read and can
# be used as a regular python value. If an exception occurs, it is set as the
# result of the function, where it can be handled as appropiate.
#
# This example assumes that the python module dill for reading and writing
# python values to files, and that the Work Queue workers are being executed in
# an appropiate python environment.
#

import dill
import logging
import os
import sys
import tempfile

import work_queue as wq

logger = logging.getLogger()
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')


def create_work_queue_task(task_counter, tmpdir, function, input_args, fn_wrapper='mdsim.py'):
    """ Returns a Work Queue task to execute the python code output = function(*input_args)
    The python function and input arguments are written to files in the
    directory tmpdir/ using dill to serialize them. These files are used as
    inputs to the Work Queue task.

    The Work Queue task executes the python function as a shell command using
    the fn_wrapper (mdsim.py by default), which reads the input files, converts
    them to valid python values, and writes to a file the python value obtained
    from the function evaluation. This output file is sent back to the Work
    Queue manager, where it can be read and decoded to obtained a valid python
    value. Should an exception occur, it is returned as the value of the function.
    """
    logger.debug("creating task {}: {}({})".format(task_counter, function.__name__, ','.join(str(arg) for arg in input_args)))

    args_file = os.path.join(tmpdir, "input_args_{}.p".format(task_counter))
    fn_file   = os.path.join(tmpdir, "function_{}.p".format(task_counter))
    out_file   = os.path.join(tmpdir, "out_{}.p".format(task_counter))

    # Save args to a dilled file.
    with open(args_file, "wb") as wf:
        dill.dump(input_args, wf)

    # Save the function to a dilled file.
    with open(fn_file, "wb") as wf:
        dill.dump(function, wf)

    # Base command just invokes python on the function and data.
    command = "./{wrapper} {fn} {args} {out}".format(
            wrapper=os.path.basename(fn_wrapper),
            fn=os.path.basename(fn_file),
            args=os.path.basename(args_file),
            out=os.path.basename(out_file))

    task = wq.Task(command)
    task.specify_tag(str(task_counter))

    task.specify_input_file(fn_wrapper, cache=True)
    task.specify_input_file(fn_file, cache=False)
    task.specify_input_file(args_file, cache=False)
    task.specify_output_file(out_file, cache=False)

    task.specify_cores(1)
    task.specify_memory(250) #MB
    task.specify_disk(250)   #MB

    return task


def report_task_result(tmpdir, task):
    """ Returns the python value obtained by evaluating the python function by
    the given task.  If the task failed, a NoResult() exception is assigned to
    the result of the function evaluation.
    """

    if task.result == wq.WORK_QUEUE_RESULT_SUCCESS:
        if task.return_status != 0:
            log.warning("task {} had non-zero exit code: {}".format(task.tag, task.return_status))
        try:
            with open(os.path.join(tmpdir, "out_{}.p".format(task.tag)), 'rb') as f:
                fn_result = dill.load(f)
        except Exception as e:
            fn_result = e
    else:
        logger.warning("no result for task {}. error code {} {}".format(task.tag, task.result, task.result_str))
        fn_result = NoResult()

    if isinstance(fn_result, Exception):
        print("task {} with exception: {}".format(task.tag, repr(fn_result)))
    else:
        print("task {} with output: {}".format(task.tag, fn_result))


def application_function(x, y):
    """ Example function to be executed remotely. """
    return y/x


class NoResult(Exception):
    """ Exception used as the result of a function evaluation of a task that failed. """
    def __repr__(self):
        return 'NoResult()'
    def __str__(self):
        return 'NoResult'

if __name__ == '__main__':
    with tempfile.TemporaryDirectory() as tmpdir:
        q = wq.WorkQueue(port=9123, debug_log='debug.log', transactions_log='tr.log')

        task_counter = 0
        total_tasks = 5

        for i in range(total_tasks):
            task = create_work_queue_task(
                    task_counter,
                    tmpdir,
                    application_function,
                    input_args=[i, 100]) # all tasks compute application_function(i, 100) which is 100/i
            q.submit(task)
            task_counter += 1

        while not q.empty():
            t = q.wait(5)
            if t:
                report_task_result(tmpdir, t)

