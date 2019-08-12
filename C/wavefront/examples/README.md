The input rows and columns are a sequence from 0 to 9. The function that
wavefront applies is simply the sum of xfile, yfile and dfile.

SUM TEST
========

Prepare
-------

	rm -f $TEST_INPUT
	rm -f R.*.*
	./gen_ints_wf.sh $TEST_INPUT 10

Run
---

	../src/wavefront ./sum_wf.sh 9 9

	value=`cat R.9.9 | sed -n 's/[[:blank:]]*\([[:digit:]]*\).*/\1/p'`
	echo "Computed value is $value"

Expected answer : 1854882

Clean
-----

	rm -f $TEST_INPUT
	rm -f R.*.*


Master Test
===========

TEST_INPUT=test.wmaster.input
TEST_OUTPUT=test.wmaster.output
PORT_FILE=master.port
MASTER_PID=master.pid
MASTER_LOG=master.log
MASTER_OUTPUT=master.output

Clean
-----

	rm -f $TEST_INPUT
	rm -f $TEST_OUTPUT
	rm -f $PORT_FILE
	rm -f $MASTER_PID
	rm -f $MASTER_LOG
	rm -f $MASTER_OUTPUT

Prepare
-------
	./gen_ints_wfm.sh $TEST_INPUT 10

Run
---

	echo "starting wavefront master"
	wavefront_master -d all -o $MASTER_LOG -Z $PORT_FILE ./sum_wfm.sh 10 10 $TEST_INPUT $TEST_OUTPUT > $MASTER_OUTPUT &
	pid=$!
	echo $pid > $MASTER_PID

	echo "waiting for port file to be created"
	wait_for_file_creation $PORT_FILE 5

	echo "running worker"
	work_queue_worker --timeout 2 localhost `cat $PORT_FILE`

	echo "extracting result"
	value=`sed -n 's/^9 9 \([[:digit:]]*\)/\1/p' $TEST_OUTPUT`

	echo "Computed value is $value"
	

Expected answer : 1854882

Clean
-----

	if [ -f $MASTER_PID ]
	then
		kill -9 `cat $MASTER_PID`
	fi

	cleanfiles

