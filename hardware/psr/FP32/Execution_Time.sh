#!/bin/bash

# Compile and run the main program
gcc PSR_Execution_Time.c -o main -I. -DARMZYNQ -lm
./main
rm -f main