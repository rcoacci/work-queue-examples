################################################################################
#
# install work queue cctools and dependencies:
#
# conda create --yes --name work_queue_environment python=3.8 dill
# conda install --yes --name work_queue_environment --channel conda-forge ndcctools
# conda activate work_queue_environment
# python python-fn-in-wq.py
#

import dill
import logging
import os
from os.path import basename
import sys
import tempfile

import work_queue as wq

logger = logging.getLogger()
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')


def create_work_queue_task(task_counter, tmpdir, function, input_args, fn_wrapper='exec_python_fn.py'):

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
            wrapper=basename(fn_wrapper),
            fn=basename(fn_file),
            args=basename(args_file),
            out=basename(out_file))

    task = wq.Task(command)
    task.specify_tag(str(task_counter))

    task.specify_input_file(fn_wrapper, cache=True)
    task.specify_input_file(fn_file, cache=False)
    task.specify_input_file(args_file, cache=False)
    task.specify_output_file(out_file, cache=False)

    return task


def report_task_result(tmpdir, t):
    if t.result == wq.WORK_QUEUE_RESULT_SUCCESS:
        if t.return_status != 0:
            log.warning("task {} had non-zero exit code: {}".format(t.tag, t.return_status))
        try:
            with open(os.path.join(tmpdir, "out_{}.p".format(t.tag)), 'rb') as f:
                fn_result = dill.load(f)
        except Exception as e:
            fn_result = e
    else:
        logger.warning("no result for task {}. error code {} {}".format(t.tag, t.result, t.result_str))
        fn_result = NoResult()

    if isinstance(fn_result, Exception):
        print("task {} with exception: {}".format(t.tag, repr(fn_result)))
    else:
        print("task {} with output: {}".format(t.tag, fn_result))

def application_function(x, y):
    return y/x


class NoResult(Exception):
    def __repr__(self):
        return 'NoResult()'
    def __str__(self):
        return 'NoResult'

if __name__ == '__main__':
        #with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir='here'
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

