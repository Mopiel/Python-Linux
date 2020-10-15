#!/usr/bin/env python3

import json
try:
    with open('dev/data.json') as f:
      data = json.load(f)
      password = data["password"]


    print("Enter Password")
    for i in range(3):
        inputPassword = input()
        if(inputPassword == password):
            print("Password correct")
            break
        if(i != 2):
            print("Wrong password try again")
        else:
            print("All possible trials were used")
except:
    print("No file with saved code")