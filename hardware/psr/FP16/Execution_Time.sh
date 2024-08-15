#!/bin/bash

# Compile and run the main program
gcc PSR_FP16_Execution_Time.c -o main -I. -DARMZYNQ -lm
./main
rm -f main
