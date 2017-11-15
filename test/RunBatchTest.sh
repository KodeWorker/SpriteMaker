#!bin/bash
read -rep "Unit test directory: >>" dir
python BatchTest.py ${dir}
$SHELL