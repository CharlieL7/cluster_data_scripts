#usr/bin/env python3
"""
Copies data up to a timestep
Uses the filenames, so does not read the files; significantly faster than reading the file.
"""
import glob
import os
import argparse as argp
from shutil import copy

def main():
    parser = argp.ArgumentParser(description="Copies folder full of mesh data files with a timestep multiple (thin copy)")
    parser.add_argument("in_dir", help="folder of mesh data files")
    parser.add_argument("out_dir", help="folder to put thinnly copied mesh data files")
    parser.add_argument("end_ts", help="ending timestep to copy to, inclusive")
    args = parser.parse_args()
    in_dir = args.in_dir
    os.path.join(in_dir, '') # add ending slash if needed
    out_dir = args.out_dir
    end_ts = int(args.end_ts)
    file_list = sorted(glob.glob(in_dir + '*.dat'))
    for f in file_list:
        fn = os.path.basename(f)
        num = ''.join(i for i in fn if i.isdigit())
        num = int(num)
        if num <= end_ts:
            copy(f, out_dir)

if __name__ == "__main__":
    main()
