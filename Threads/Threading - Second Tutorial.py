# Thread sync. waiting for threads to finish before program continues.
from threading import Thread
import time

ls = []

def count(n):
    for i in range(1, n+1):
        print(i)
        ls.append(i)
        time.sleep(0.01)

def count2(n):
    for i in range(1, n+1):
        print(i)
        ls.append(i)
        time.sleep(0.02)

thread = Thread()

if not thread.is_alive():
    print("Starting Thread")

thread = Thread(target=count, args=(10,))
thread.start()

if thread.is_alive():
    print("Thread Started")
# if we put a join here, we allow one thread to finish running before the other one begins

y = Thread(target=count2, args=(15,))
y.start()

print("Done")

# do not move past this line until the threads stops running
thread.join()
y.join()

print(ls)