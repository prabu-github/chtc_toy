#!/bin/bash

DATAFILE=$1
PARAM=$2
OUTDIR=$3

python main.py --data_file $DATAFILE --out_dir $OUTDIR --param $PARAM