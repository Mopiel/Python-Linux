#!/usr/bin/env python3

import json


password = input("Input Password first time\n")
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