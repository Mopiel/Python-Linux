#!/usr/bin/env python3

import os
DIR = './jpgFiles'


try:
    for filename in os.listdir(DIR):
        infilename = os.path.join(DIR, filename)
        if not filename.endswith(".jpg"): continue
        oldbase = os.path.splitext(filename)
        newname = infilename.replace('.jpg', '.png')
        output = os.rename(infilename, newname)
except:
    print("Something went wrong")