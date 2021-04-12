Work Queue Replica Exchange
---------------------------

This program implements the replica exchange ensemble method
using the Work Queue framework and the Protomol molecular dynamics
kernel.  An example execution is provided with the WW protein
as a test input.

Please cite this work as follows:
- Dinesh Rajan, Anthony Canino, Jesus A Izaguirre, and Douglas Thain, "Converting a High Performance Application to an Elastic Cloud Application", The 3rd IEEE International Conference on Cloud Computing Technology and Science", November 2011.

Installation
------------

- Install the [Work Queue](http://ccl.cse.nd.edu/software/workqueue) execution framework.

- Install the [ProtoMol](https://simtk.org/projects/protomol) molecular dynamics toolkit.

Example Application
-------------------

First start the manager program, indicating the simulation and replication
configuration.  This example runs the replica exchange simulations on the WW protein with 30 replicas using temperatures between 300 and 400F:

    ./wq_replica_exchange.py ww_exteq_nowater1.pdb ww_exteq_nowater1.psf par_all27_prot_lipid.inp  300 400  30

The manager program will create and distribute tasks to remote workers.
You must then start one or more workers as follows:

    work_queue_workers -d all <HOSTNAME> <PORT>

where <HOSTNAME> is the name of the host on which the master is running <PORT> is the port number on which the master is listening.

Alternatively, you can also specify a project name for the master and use that
to start workers:

    ./wq_replica_exchange -N REPEXCH ww_exteq_nowater1.pdb ww_exteq_nowater1.psf par_all27_prot_lipid.inp  300 400  30
    work_queue_worker -d all -N REPEXCH

When the application completes, you will find all the output files in the
simfiles directory (or the directory specified in the -p option).
