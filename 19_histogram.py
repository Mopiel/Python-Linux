import matplotlib.pyplot as plt
import imageio
from threading import Thread
import time
import numpy as np

picture=imageio.imread("hist/car.jpg")

plt.figure(1,figsize=(15,15))
plt.imshow(picture)



hight=len(picture)
width=len(picture[0])

print("Pixels",width,"x",hight)


RGB= []

def calculate(z):
    listTones = []
    for i in range(width):
        for j in range(hight):
            listTones.append(picture[j,i,z])
    returnList =[]
    for n in range(255):
        returnList.append(listTones.count(n))
    RGB.append(returnList)



threads = []

for z in range(3):
    processThread = Thread(target=calculate, args=[z])
    processThread.start()
    threads.append(processThread)

for thread in threads:
    thread.join()

print("done")

yLabel = []

for y in range(255):
    yLabel.append(y)

for x,colors in enumerate(RGB):
    plt.figure(x+2)
    plt.title("Histogram")
    plt.plot(yLabel,colors, color='b')
    plt.xlabel("Color {}".format(x))

plt.show()
