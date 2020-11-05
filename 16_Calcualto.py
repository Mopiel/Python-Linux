from ComplexNumber import Complex
import sys

import re
data = input("Put mathematical equation like '1+2-4i*(34+4i)' where i is imag\n")
newdata = re.split('(-|\(|\)|\+|\*|/)', data)
for id,d in enumerate(newdata):
    if(len(d) and d[-1] == "i"):
        newdata[id] = "Complex(0,{})".format(d[0:-1])
    elif(d.isdigit()):
        newdata[id] = "Complex({},0)".format(d)

newdata = "".join(newdata)
print(data,"=",eval(newdata))

