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

print('Maximum RGB tones in this image {}'.format(picture.max()))
print('Minimum RGB tones in this image {}'.format(picture.min()))

print("Piksel dimension of picutre ",width," x ",hight)


RGB= []

def calculate(z):
    list_tones = []
    for i in range(0,width):
        for j in range(0,hight):
            list_tones.append(picture[j,i,z])
    RGB.append(list_tones)


threads = []

for z in range(3):
    print("one")
    processThread = Thread(target=calculate, args=[z])
    processThread.start()
    threads.append(processThread)

for thread in threads:
    thread.join()

print("done")


for x,colors in enumerate(RGB):
    plt.figure(x+2)
    plt.title("Histogram")
    plt.hist(colors, 255, color='b')

    plt.xlabel("Kolor {}".format(x))

plt.show()
