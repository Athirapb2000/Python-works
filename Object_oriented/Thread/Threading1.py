"""
THREAD
Thread means part of a program or lightweight process.Mainly two types of threading
1. Simple Threading
2. Multiple Threading
"""
# Python Threads
from time import sleep
def task():
    # block for a moment
    sleep(3)
    # display a message
    print('This is from another thread')
# task()

from threading import Thread
# create a thread
thread = Thread(target=task)
# Next, we can create an instance of the threading.Thread class and specify
# our function name as the 'target' argument in the constructor.
# run the thread
thread.start()
