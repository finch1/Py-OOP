from threading import Thread
import time

def count(n):
    for i in range(1, n+1):
        print(i)
        time.sleep(0.01)

def count2(n):
    for i in range(1, n+1):
        print(i)
        time.sleep(0.02)

x = Thread(target=count, args=(10,))
x.start()

y = Thread(target=count2, args=(15,))
y.start()

print("Done")