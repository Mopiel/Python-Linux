import argparse
import math

parser = argparse.ArgumentParser(description='Put --a,--b and --c arguments.')
parser.add_argument("--a", type=int, default=1)
parser.add_argument("--b", type=int, default=1)
parser.add_argument("--c", type=int, default=1)

args = parser.parse_args()

a = args.a
b = args.b
c = args.c

d = b**2 -4*a*c
if(d<0):
    print("Equation has no solution")
else:
    sd = math.sqrt(d)
    x1 = (-b-sd)/(2*a)
    x2 = (-b+sd)/(2*a)
    if(x1==x2):
        print("x=",x1)
    else:
        print("x1=",x1)
        print("x2=",x2)