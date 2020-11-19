from Philosophers import *

forks = []
philosophers = []

philosophersNumber = 5
waiter = Deadlock(philosophersNumber-1)


for i in range(0, philosophersNumber):
    forks.append(Fork(i))

for i in range(0, philosophersNumber):
    philosophers.append(Philosopher(i, forks[i], forks[(i+1)%philosophersNumber], waiter))
    philosophers[i].start()
