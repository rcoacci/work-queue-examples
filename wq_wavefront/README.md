Wavefront Manual
----------------

<table>
<tr>

<td>
<a href=images/wavefront_large.gif><img src=images/wavefront_small.gif align=right border=0></a>
</td>

<td>
Wavefront( array R[x,0], array R[0,y], function F(x,y,d) )<br>
returns matrix R where<br>
R[i,j] = F( R[i-1,j], R[i,j-1], R[i-1,j-1] )<br>
</td>

</tr>
</table>

The Wavefront abstraction computes a two dimensional recurrence relation.
You provide a function F that accepts the left (x), right (y), and diagonal (d).
The abstraction then runs each of the functions in the order of dependency,
handling load balancing, data movement, fault tolerance, and so on.

Please cite this paper for the Wavefront abstraction:

- Li Yu, Christopher Moretti, Andrew Thrasher, Scott Emrich, Kenneth Judd, and Douglas Thain, <a href=http://ccl.cse.nd.edu/research/papers/abstr-jcc.pdf>Harnessing Parallelism in Multicore Clusters with the All-Pairs, Wavefront, and Makeflow Abstractions</a>, Journal of Cluster Computing, 13(3), pages 243-256, September, 2010. DOI: 10.1007/s10586-010-0134-7


Getting Started
---------------

To use Wavefront, first install the <a href="http://ccl.cse.nd.edu/software/downloadfiles.shtml">Cooperative Computing Tools</a> into your home directory, like so:

    git clone https://github.com/cooperative-computing-lab/cctools.git cctools-src
    cd cctools-src
    ./configure --prefix ${HOME}/cctools
    make install
    export PATH=${HOME}/cctools/bin:${PATH}
    cd ..

Then clone this example repository and build wavefront like so:

    git clone https://github.com/cooperative-computing-lab/work-queue-examples.git
    cd work-queue-examples/wq_wavefront
    make

Note that this builds three different programs:
- wavefront_manager - The WQ manager program for running a wavefront application.
- example.func - A sample function that computes a Nash equilibrium.
- wavefront - An alternate implementation of wavefront that submits individual batch jobs.

Using Wavefront
---------------

You need to set up an
input file with initial boundary values of R, and provide a function that
computes a new cell from adjacent cells. Each line of the input file has the format:

    row column arg1,arg2,...

In which row and column describe the position of a cell, with zero-based
indices, and arg1,arg2,... is the list of arguments fed to F (that is, each
R[i,j] is actually a tuple).

To run wavefront, specifying the program that computes each cell, and the
number of cells in each dimension, for example:

    wavefront_manager ./func.exe 10 10 input.data output.data

in which input.data is the file with the initial boundary conditions,
and output.data are the results computed for a 10x10 matrix.

The program `func.exe` may be written in any language that you like.
For each cell of the result, the program will be invoked like this:

    ./func.exe x y x-file y-file d-file

in which each of `x-file`, `y-file` and `d-file` are files
that contain the data from
the x, y, and diagonal neighbors, in the format:

    arg1,arg2,...

These files are generated automatically by `wavefront_manager`. Your
function is required to parse them, and to print the result of the current cell
to `stdout`, in the format:

    arg1,arg2,...

`wavefront_manager` is a Work Queue application, thus it does not perform
any work by itself, but it relies on workers connecting to it. To launch a
single worker:

    work_queue_worker mymachine.somewhere.edu 9123

in which 9123 is the default port for Work Queue applications. Work Queue
provides convenient alternatives to launch many workers simultaneously for
different batch systems (e.g. condor), which are explained in the section <b>
    Project names </b> in the <a href=workqueue.html> Work Queue manual </a>.

Wavefront will check for a few error conditions, and then start to run,
showing progress on the console like this:

    # elapsed time : waiting jobs / running jobs / complete jobs (percent complete)
    0 : 0 / 1 / 0 (%0.00)
    5 : 0 / 2 / 1 (%1.23)
    10 : 0 / 3 / 3 (%3.70)
    16 : 0 / 4 / 6 (%7.41)
    21 : 0 / 4 / 8 (%9.88)
    ...

When complete, your outputs will be stored in the output file specified, with the same format as for the input data.

Example
--------


This is an example problem to use with the Wavefront abstraction.

This directory contains a toy problem provided by Dr. Kenneth Judd
at Stanford University.  It represents a common category of problems
found in economics.  The function computes the Nash equilibrium between
two players in a game.

To run the sample problem, start the Wavefront manager process,
specify the size of the problem, the function, the input data,
and where to place the output data:

    wavefront_manager example.func 10 10 example.input.data example.output.data

Then, start one or more worker processes, and tell them to contact
the manager process using host name and port number:

    work_queue_worker mymachine.somewhere.edu 9123

The manager process will then output a series of lines detailing the
progress of the entire computation.  If the manager fails or is killed,
it can simply be restarted with the same command.  It will read in the
already completed work, and continue where it left off.

Enough input is provided for a problem of up to 500x500.

Each function call takes about 5 seconds to execute on a modern
desktop processor.  Sequentially the problem is O(n^2).  By adding
workers, you can parallelize the work into O(n) time.

    Problem   Sequential  Parallel
    size            time      time
    ------------------------------
    10x10           500s       50s
    100x100       50000s      500s
    500x500     1250000s     2500s

Visualizing Results
-------------------

Here is a graph of a 100 by 100 problem run on a 64-core machine, where each F takes about five seconds to execute:

<img src=images/wavefront_progress.gif>

The <b>-B</b> option will write a bitmap progress image every second.
Each pixel represents the state of one cell in the matrix: green indicates complete, blue currently running, yellow ready to run, and red not ready.  Here is an example of the progress of a small ten by ten job using five CPUs:

<table>
<tr>
<td><img src=images/wavefront_progress1.gif>
<td><img src=images/wavefront_progress2.gif>
<td><img src=images/wavefront_progress4.gif>
<td><img src=images/wavefront_progress5.gif>
</table>

Note that at the broadest part of the workload, there are not enough CPUs to run all cells at once, so some must wait.  Also note that the wave does not need to run synchronously: cells may begin to compute as soon as their dependencies are satisfied.

For More Information
--------------------

For the latest information about Wavefront, please visit our <a href="http://ccl.cse.nd.edu/software/wavefront">web site</a> and subscribe to our <a href="http://ccl.cse.nd.edu/software">mailing list</a>.
