import time
import threading
import os, random

numForks = 5
numPhilosophers = 5
count = 0

class Philosopher(threading.Thread):
    
    def __init__(self, index):
        super().__init__()
        self.index = index
        self.leftFork = forks[self.index]
        self.rightFork = forks[(self.index + 1) % numForks]

    def run(self):
        global count
        while True:
            if self.leftFork.index > self.rightFork.index:
                firstFork = self.rightFork
                secondFork = self.leftFork
                
            else:
                firstFork = self.leftFork
                secondFork = self.rightFork
                

            firstFork.pickup()
            result_list.append([self.index, 2, 1])
            secondFork.pickup()
            result_list.append([self.index, 1, 1])
            
            self.eat()

            secondFork.putdown()
            result_list.append([self.index, 1, 2])
            firstFork.putdown()
            result_list.append([self.index, 2, 2])
            
            self.thinking()
            result_list.append([self.index, 0, 3])
            count += 1
            if count >= n:
                break
            
    def eat(self):
        # print ("Philosopher", self.index, " starts to eat.")
        time.sleep(random.choice([1, 2, 3]))
        # print ("Philosopher", self.index, " finishes eating and leaves to think.")

        print(result_list)

    def thinking(self):
        time.sleep(random.choice([1, 2, 3]))

class Fork():
    def __init__(self, index):
        self.index = index
        self._lock = threading.Lock()
        
    def pickup(self):
        self._lock.acquire()

    def putdown(self):
        self._lock.release()

if __name__ == '__main__':
    #创建叉子与哲学家实例
    forks = [Fork(idx) for idx in range(numForks)]
    philosophers = [Philosopher(idx) for idx in range(numPhilosophers)]

    result_list=[]

    # 方便 CTRL + C 退出程序
    try:
        n = int(input('请输入 0 到 60 的整数:'))
        if 0 <= n <= 60:
            #开启所有的哲学家线程
            count = 0
            for philosopher in philosophers:
                philosopher.start()              
    except Exception as e:
        raise "输入的不是 0 到 60 的整数"