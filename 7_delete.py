#!/usr/bin/env python3

import json

change = [" i "," się "," oraz "," dlaczego "]

try:
    with open('texts/text_1.txt',"r",encoding="utf-8") as f:
        text = f.read()
        print(text)
        for i in change:
            text = text.replace(i," ")
        print("------------------------------------------------")
        print(text)


except:
    print("No file with saved code")