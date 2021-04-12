#!/bin/sh

cat "$TEST_INPUT" | awk -F"/" '{print $3}'
howmany() { echo $#;}
num_files=$(howmany $in_files)
for i in $in_files; do
  count=`awk '{print $1}' $TEST_OUTPUT | grep -c $i`
  if [ $num_files != $count ]
  then
	exit 1
  fi
  count=`awk '{print $2}' $TEST_OUTPUT | grep -c $i`
  if [ $num_files != $count ]
  then
	exit 1
  fi
done

