#usr/bin/env python3
"""
Copies data thinnly (every mod timesteps) and/or with truncation to new folder.
Can also just copy all the data directly.
Uses the filenames, so does not read the files; significantly faster than reading the file.
"""
import glob
import os
import argparse as argp
from pathlib import Path
from shutil import copy

def main():
    parser = argp.ArgumentParser(
        description="Copies folder full of mesh data files"+
        "with a timestep multiple (thin copy)"
    )
    parser.add_argument("in_dir", help="folder of mesh data files")
    parser.add_argument("out_dir", help="folder to put thinnly copied mesh data files")
    parser.add_argument("-m", "--mod", help="modulus for thin copy")
    parser.add_argument("-e", "--end_ts", help="ending timestep to copy to, inclusive")
    args = parser.parse_args()
    in_dir = args.in_dir
    os.path.join(in_dir, '') # add ending slash if needed
    out_dir = args.out_dir
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    file_list = sorted(glob.glob(in_dir + '*.dat'))
    for f in file_list:
        fn = os.path.basename(f)
        num = ''.join(i for i in fn if i.isdigit())
        num = int(num)
        if args.mod and args.end_ts:
            mod = int(args.mod)
            end_ts = int(args.end_ts)
            if num % mod == 0 and num <= end_ts:
                copy(f, out_dir)
        elif args.mod:
            mod = int(args.mod)
            if num % mod == 0:
                copy(f, out_dir)
        elif args.end_ts:
            end_ts = int(args.end_ts)
            if num <= end_ts:
                copy(f, out_dir)
        else:
            copy(f, out_dir)

if __name__ == "__main__":
    main()
