Work Queue Pi Example
---------------------

This program is a simple example of how to use Work Queue
with PythonTasks.  It estimates the value of pi by estimating
the ratio of the areas of a circle inscribed in a square.

To run:

1. Install CCTools. For example, using conda:
conda install -c conda-forge ndcctools

2. Run the manager program:
python wq_pi_example.py 100 100000

3. Start one or more workers:
work_queue_worker localhost 9123

