
from pathlib import Path
import argparse
import numpy as np
import pandas as pd
import torch
from argparse import ArgumentParser

from params import *

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--data_file',
                        type=str,
                        required=True,
                        action='store')
    parser.add_argument('--param',
                        type=str,
                        default='double',
                        action='store')
    parser.add_argument('--out_dir',
                        type=str,
                        required=True,
                        action='store')
    args = parser.parse_args()
    data_file = Path(args.data_file).resolve()
    factor = PARAMS[args.param]
    out_dir = Path(args.out_dir).resolve()
    
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir/f'{data_file.name}_X{int(factor)}.pt'
    
    t = torch.load(data_file)
    tout = t*factor
    torch.save(tout, out_file)
