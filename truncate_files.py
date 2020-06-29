#!usr/bin/env python3
import glob
import sys
import os
import csv

"""
truncates data files past a certain time
Dangerous script, removes files permanentantly
"""
def main():
    """
    usage: (parent directory with folders of data, number of cycles to truncate past)
    """
    parent_dir = sys.argv[1]
    num_cycles = float(sys.argv[2])
    child_folders = sorted(glob.glob(parent_dir + "*/"))
    for c_folder in child_folders:
        file_list = glob.glob(c_folder + '/*.dat')
        file_list = sorted(file_list)
        for dat in file_list:
            with open(dat, 'r') as f:
                reader = csv.reader(f, delimiter=' ')
                is_header = True
                while is_header:
                    tmp = next(reader)
                    if tmp[0] == "#":
                        if len(tmp) == 4:
                            var_name = tmp[1]
                            data_val = tmp[3]
                            if var_name == "time":
                                time_file = float(data_val)
                            if var_name == "De":
                                De_file= float(data_val)
                    else:
                        is_header = False
            try:
                cycle_period = 1 / De_file
                tot_time = num_cycles * cycle_period
                if time_file > tot_time:
                    os.remove(dat)
            except NameError as e:
                print("One of the required variables was not instantiated: {}".format(e))

if __name__ == "__main__":
    main()
