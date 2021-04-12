
<img align=center src=images/wavefront_large.gif width=512></img>


Wavefront User's Manual
-----------------------

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

Getting Started
---------------

If you have not done so already, please clone this examples repository like so:

    git clone https://github.com/cooperative-computing-lab/work-queue-examples.git
    cd ./C/wavefront

To use Wavefront, first install the <a
    href="http://ccl.cse.nd.edu/software/downloadfiles.shtml">Cooperative Computing Tools</a>.
If you want to build from source:

    git clone https://github.com/cooperative-computing-lab/cctools.git
    cd ./cctools
    ./configure --prefix ${PWD}
    make clean
    make install
    export PATH=${PWD}/bin:${PATH}
    cd ..


This will build Work Queue and other required libraries needed by Wavefront.
Next we need to build `wavefront_master`, which requires knowing the location of
CCTools and where you want wavefront installed. This is specified in `config.mk`:

    echo CCTOOLS_INSTALL_DIR=${PWD}/cctools/ > config.mk
    echo WAVEFRONT_INSTALL_DIR=${PWD}/ >> config.mk

Once specified in `config.mk` we can now build the software:

    make install
    export PATH=${PWD}/bin:${PATH}

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

	wavefront_master ./func.exe 10 10 input.data output.data

in which input.data is the file with the initial boundary conditions,
and output.data are the results computed for a 10x10 matrix.

The program `func.exe` may be written in any language that you like.
For each cell of the result, the program will be invoked like this:

	./func.exe x y x-file y-file d-file

in which each of `x-file`, `y-file` and `d-file` are files
that contain the data from
the x, y, and diagonal neighbors, in the format:

	arg1,arg2,...

These files are generated automatically by `wavefront_master`. Your
function is required to parse them, and to print the result of the current cell
to `stdout`, in the format:

	arg1,arg2,...

`wavefront_master` is a Work Queue application, thus it does not perform
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

To run Wavefront, you need to set up an input file with the
initial boundary values of M, and provide a function that computes
a new cell from the adjacent cells.  The abstraction will produce
an output file with all of the values of the matrix.

This directory contains a toy problem provided by Dr. Kenneth Judd
at Stanford University.  It represents a common category of problems
found in economics.  The function computes the Nash equilibrium between
two players in a game.

Before starting this example move to the correct directory:

    cd examples

Compile the example function like this:

    gcc example.func.c -o example.func -lm

To run a sample problem, start the Wavefront master process,
specify the size of the problem, the function, the input data,
and where to place the output data:

    wavefront_master example.func 10 10 example.input.data example.output.data

Then, start one or more worker processes, and tell them to contact
the master process using host name and port number:

    work_queue_worker mymachine.somewhere.edu 9068

The master process will then output a series of lines detailing the
progress of the entire computation.  If the master fails or is killed,
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


Another Example
---------------

In this example, we will compare the setup and execution of
local and distributed wavefront 
(`wavefront` and wavefront_master` respectively).

The input rows and columns are a sequence from 0 to 9. The function that
wavefront will apply simply sums the values of the xfile, yfile and dfile.

For both the local and distributed execution we have the same initial step:

    cd examples


### Local Wavefront

#### Prepare

As the local version of `wavefront` functions more as a test, the inputs are required to be prefixed with `R`

    cd local
	./gen_ints_wf.sh R 10

#### Run

	wavefront ./sum_wf.sh 9 9

    cat R.9.9 | sed -n 's/[[:blank:]]*\([[:digit:]]*\).*/\1/p'

Expected answer : 1854882

#### Clean

	rm -f R.*.*


### Master Test
#### Prepare

    cd dist
	./gen_ints_wfm.sh dist_input.dat 10

#### Run

	wavefront_master -d all -o wf_master.log -p 9123 ./sum_wfm.sh 10 10 dist_input.dat dist_output.dat

In a seperate terminal or in the background we need to run a worker to execute the tasks.

	work_queue_worker --timeout 2 localhost 9123

Once the master is completed, we need to find the final data point:

	sed -n 's/^9 9 \([[:digit:]]*\)/\1/p' dist_output.dat

Expected answer : 1854882

#### Clean

    rm -rf dist_input.dat dist_output.dat wf_master.log 

For More Information
--------------------

For the latest information about Wavefront, please visit our <a href="http://ccl.cse.nd.edu/software/wavefront">web site</a> and subscribe to our <a href="http://ccl.cse.nd.edu/software">mailing list</a>.

Last edited: August 2019
Moved to Github: August 2019

Wavefront is Copyright (C) 2010- The University of Notre Dame.
All rights reserved.
This software is distributed under the GNU General Public License.
See the file COPYING for details.


