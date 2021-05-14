#! /usr/bin/env python3
#
# This wrapper executes python function evaluations from the shell.
# Use as:
# mdsim.py fn_file args_file out_file
#
# in which
#   fn_file is a file that contains a function serialized (using dill).
#   args_file is a file that contains the seriallized arguments to the
#    function.
#  out_file is the name of a file to which the results of the function
#    evaluation will be serialized.
#
# If the function evaluation raises an exception, the exception is written to
# out_file as the result.
#

import os
import sys
import dill

# import some other packages used by the actual application, e.g.:
import math

(fn, arg, out) = sys.argv[1], sys.argv[2], sys.argv[3]

with open(fn, "rb") as f:
    exec_function = dill.load(f)
with open(arg, "rb") as f:
    exec_args = dill.load(f)

try:
    exec_out = exec_function(*exec_args)
except Exception as e:
    exec_out = e

with open(out, "wb") as f:
    dill.dump(exec_out, f)

