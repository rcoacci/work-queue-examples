Work Queue BWA
--------------

The wq_bwa.py program aligns sequences of genomes listed in a fastq file using
the Burrows-Wheeler Aligner. It aligns by partitioning the file into pieces
containing one or more sequences and running BWA to align them individually.
The program uses the Work Queue framework for distributed execution.

Installation
------------

- Install the [Work Queue](http://ccl.cse.nd.edu/software/workqueue) framework.
- Install BWA and its required dependencies from http://bio-bwa.sourceforge.net

Example
-------

First start the manager program, which will divide up the queries
and generate a large number of tasks:

    ./wq_bwa <REFERENCE_FILE> <FASTQ_FILE>

Then, run one or more remote workers:

    work_queue_worker -d all <HOSTNAME> <PORT>

where <HOSTNAME> is the name of the host on which the master is running
	  <PORT> is the port number on which the master is listening.

Alternatively, you can also specify a project name for the master and use that
to start workers:

    ./wq_bwa <REFERENCE_FILE> <FASTQ_FILE> -N WQBWA
    work_queue_worker -d all -N WQBWA
