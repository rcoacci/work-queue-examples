#!/usr/bin/env python

# This program is a simple example of how to use Work Queue.
# It estimates Pi by computing the ratio of the areas of a circle in a square.
# It accepts two parameters: number of tasks and number of random points to generate per tasks.
# Example Use: python wq_pi_example.py 100 100000

import work_queue as wq
import sys
import os

num_of_tasks = int(sys.argv[1])
points_per_task = int(sys.argv[2])
total_points_in_square = 0
total_points_in_circle = 0

# Define a function to approximate pi using "count" points.
# Returns a tuple giving the number of points inside and outside a circular arc.
# Note that the necessary imports must be given inside the function body.

def approx_pi( count ):
    import math
    import random

    ninside = 0
    noutside = 0

    for i in range(1,count):
        x = random.random()
        y = random.random()
        if math.sqrt(x*x + y*y) <= 1.0:
            ninside+=1
        else:
            noutside+=1

    return [ninside,count]

# Main Program:
# Create a new queue listening on a fixed port.
# Submit multiple tasks, and accumulate the results.

q = wq.WorkQueue(9123)

print("Listening on port {}".format(q.port))
print("Submitting tasks...")

for i in range(num_of_tasks):
    t = wq.PythonTask(approx_pi,points_per_task)

    t.specify_cores(1)
    t.specify_memory(100)
    t.specify_disk(200)

    q.submit(t)

print("Accumulating results...")

while not q.empty():
    t = q.wait(5)
    if t:
        if t.result == wq.WORK_QUEUE_RESULT_SUCCESS and t.return_status == 0:
                points_in_circle, points_in_square = t.output
                total_points_in_square += points_in_square
                total_points_in_circle += points_in_circle
                print("Estimate: {}".format(float(4 * total_points_in_circle) / total_points_in_square))
        else:
            print("    Task could not be completed successfully: {}".format(t.output))

print("All tasks have finished.")

