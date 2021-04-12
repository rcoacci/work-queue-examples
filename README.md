# Work Queue Example Applications

This is a collection of examples of applications written using
the [Work Queue distributed application framework](http://ccl.cse.nd.edu/software/workqueue/).

Briefly, a Work Queue application consists of a manager process that coordinates
a number of worker processes running in a remote cluster, cloud, or grid.
The manager dispatches a large number of tasks, each consisting of a command
line to execute, along with an explicit set of input and output files.
As tasks complete, the manager may generate more in response.
The number of workers may scale up or down (or fail and recover)
as the application runs.

The [Work Queue API](http://ccl.cse.nd.edu/software/manuals/api/html/work__queue_8h.html)
is available in Python, Perl, and C, and so these
applications are written in various different styles and languages.
Some require specific external programs to be installed.

Python Applications:
- wq_bwa
- wq_repex 

C Applications:
- wq_allpairs
- wq_wavefront
- wq_sand
- wq_sort

Perl Applications:
- wq_maker
- wq_bowtie
