#!bin/bash
echo "Test Directories:"
ls

read -rep "Test directory: (\".\" for all) >> " dir
python BatchTest.py ${dir}
$SHELL