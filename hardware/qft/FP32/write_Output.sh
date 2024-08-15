#!/bin/bash

# Compile and run the main program
gcc QFT_FP32_Write_Output.c -o main -I. -DARMZYNQ -lm
./main
rm -f main
