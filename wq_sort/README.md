Work Queue Sort Example
-----------------------

The wq_sort program sorts a column of integers in a file by partitioning the
file into pieces and distributing them for individual sorting. The program uses
the <a href=http://ccl.cse.nd.edu/software/workqueue>Work Queue framework</a> for distributed execution on available resources.


Getting Started
---------------

First install the <a href="http://ccl.cse.nd.edu/software/downloadfiles.shtml">Cooperative Computing Tools</a> into your home directory, like so:

    git clone https://github.com/cooperative-computing-lab/cctools.git cctools-src
    cd cctools-src
    ./configure --prefix ${HOME}/cctools
    make install
    export PATH=${HOME}/cctools/bin:${PATH}
    cd ..

Then clone this example repository and build sort like so:

    git clone https://github.com/cooperative-computing-lab/work-queue-examples.git
    cd work-queue-examples/wq_sort
    make

Running Sort
------------

Run the following command:
    ./wq_sort /bin/sort sample.txt

This will begin a manager program that uses the standard 
GNU sort utility as the computation kernel and sorts the integers
in the file sample.txt.

Then, you must start one or more worker programs like this:
     work_queue_worker mymachine.somewhere.edu 9123 

Replace mymachine.somewhere.edu with the name of the machine running the manager program, and 9123 with the port number it is listening on.

When the sorting completes, you will find the output file in the same directory as where wq_sort was run.

Alternatively, you can use a "project name" to help the manager and workers connect:

    ./wq_sort -N myproject /bin/sort sample.txt
    work_queue_worker -N myproject

