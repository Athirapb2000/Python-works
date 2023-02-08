"""
Threading example
"""
import threading
def coder(number):
    print('coders:', number)
    return
threads = []
for i in range(5):
    # creating threads
    t = threading.Thread(target=coder, args=(i,))
    threads.append(t)
    # starting threads
    t.start()