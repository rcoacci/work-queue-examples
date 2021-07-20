################################################################################
#
# This example shows how to execute native python functions as Work Queue
# tasks. In particular, the python function 'application_function(x,y)' (which
# simply computes y/x) is executed remotely at workers as Work Queue task for
# various combinations of arguments.
#
# A Work Queue PythonTask is created by writing the desired function and its
# arguments to a file (i.e., serialization). At the worker, these files are
# read and the function call is executed. The output of the function is then
# serialized and sent back to the Work Queue manager, where it is read and can
# be used as a regular python value. If an exception occurs, it is set as the
# result of the function, where it can be handled as appropiate.
#

import work_queue as wq

def application_function(x, y):
	""" Example function to be executed remotely. """
	return y/x


if __name__ == '__main__':

	q = wq.WorkQueue(9123)

	total_tasks = 20

	for i in range(total_tasks):
		task = wq.PythonTask(application_function, i+1, 100) # all tasks compute application_function(i, 100) which is 100/i
		task.specify_environment('venv.tar.gz')
		q.submit(task)

	while not q.empty():
		t = q.wait(5)
		if t:
			x = t.output
			print(x)
			

