# single threading
# a custom function that blocks for a moment
from threading import Thread
from time import sleep
def task(sleep_time, message):
    # block for a moment
    sleep(sleep_time)
    # display a message
    print(message)

# create a thread
thread = Thread(target=task, args=(1.5, 'New message from another thread'))
# run the thread
thread.start()
# wait for the thread to finish
print('Waiting for the thread..')
thread.join()