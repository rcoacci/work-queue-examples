Work Queue Bowtie Example
-------------------------

The wq_bowtie program aligns sequences of genomes listed in a fastq file using
Bowtie. It aligns by partitioning the file into pieces containing one or more
sequences and running Bowtie to align them individually. The program uses the
Work Queue framework for distributed execution.

Installation
------------
- Install the [Work Queue](http://ccl.cse.nd.edu/software/workqueue) framework.
- Install Bowtie and its required dependencies from http://bowtie-bio.sourceforge.net/index.shtml

Example
-------

First start the manager program, which will partition the reference and query files into appropriate tasks:

    ./wq_bowtie.pl <REFERENCE_FILE> <FASTQ_FILE>

Then start one or more workers to execute the tasks:

    work_queue_worker -d all <HOSTNAME> <PORT>


where <HOSTNAME> is the name of the host on which the master is running and <PORT> is the port number on which the master is listening.

Alternatively, you can also specify a project name for the master and use that
to start workers:

    ./wq_bowtie <REFERENCE_FILE> <FASTQ_FILE> -M myproject
    ./work_queue_worker -d all -M myproject

When the alignment completes, you will find the output files in the
same directory from where wq_bowtie was run.
