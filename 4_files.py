#!/usr/bin/env python3

import os
DIR = './dev'
try:
    print(len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))
except:
    print("No such a file or directory: "+ DIR)