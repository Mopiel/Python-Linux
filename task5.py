#!/usr/bin/env python3

import os
DIR = './dev'

def print_files(dirpath , number=1):
    dires = [name for name in os.listdir(dirpath) if os.path.isdir(os.path.join(dirpath, name))]
    files = [file for file in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, file))]
    for f in files:
        print("  "*number,f)
    for d in dires:
        print(d)
        print_files(dirpath+"/"+d,number+1)


try:
    print_files(DIR)
except:
    print("Something went wrong")