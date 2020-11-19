import time
import sys
import threading

timeOfActivity = 1
repititionNumber = 10

class Fork(object):
    def __init__(self, id):
        self.id = id
        self.user = None
        self.taken = False
        self.lock = threading.Condition(threading.Lock())

    def drop_fork(self, user):
        with self.lock:
            while self.taken == False:
                self.lock.wait()
            self.user = None
            self.taken = False
            self.lock.notifyAll()
            print("Philosopher %s has putted back fork %s" % (user, self.id))

    def take_fork(self, user):
        with self.lock:
            while self.taken == True:
                self.lock.wait()
            self.user = user
            self.taken = True
            self.lock.notifyAll()
            print("Philosopher %s has taken fork %s"  % (user, self.id))

class Philosopher(threading.Thread):
    def __init__(self, id, leftFork, rightFork, waiter):
        threading.Thread.__init__(self)
        self.id = id
        self.leftFork = leftFork
        self.rightFork = rightFork
        self.waiter = waiter

    def grapForks(self):
        self.leftFork.take_fork(self.id)
        self.rightFork.take_fork(self.id)

    def dropForks(self):
        self.rightFork.drop_fork(self.id)
        self.leftFork.drop_fork(self.id)

    def run(self):
        for i in range(repititionNumber):
            if self.waiter:
                self.waiter.check()
            self.grapForks()
            time.sleep(timeOfActivity)
            self.dropForks()
            if self.waiter:
                self.waiter.leave()
        print("Philosopher %s finished eating and thinking"  % self.id)

class Deadlock(object):
    def __init__(self, initial):
        self.lock = threading.Condition(threading.Lock())
        self.deadlockValue = initial
        self.value = 0

    def leave(self):
        with self.lock:
            self.value -= 1
            self.lock.notify()

    def check(self):
        with self.lock:
            while self.value == self.deadlockValue:
                self.lock.wait()
            self.value += 1
