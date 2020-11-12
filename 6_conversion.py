#!/usr/bin/env python3

import os
DIR = './jpgFiles'

from PIL import Image

try:
    for filename in os.listdir(DIR):
        infilename = os.path.join(DIR, filename)
        if not filename.endswith(".jpg"): continue
        # oldbase = os.path.splitext(filename)
        # newname = infilename.replace('.jpg', '.png')
        # output = os.rename(infilename, newname)
        im1 = Image.open(os.path.join(DIR, filename))
        im1.save(os.path.join(DIR, filename.replace('.jpg', '.png')))
        os.remove(infilename)
except:
    print("Something went wrong")