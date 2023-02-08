import time
import threading
def cal_square(num):
    print('Calculate the square root of the given number')
    for n in num:
        time.sleep(0.3)              # at each iteration it waits 0.3 seconds
        print('Square is :', n*n)

def cal_cube(num):
    print('Calculate the cube of the given number')
    for n in num:
        time.sleep(0.3)
        print('Cube is :', n*n*n)

arr = [4, 5, 6, 7, 2]   # given array or list

t1 = time.time()  # get total time to execute the function
th1 = threading.Thread(target=cal_square, args=(arr,))
th2 = threading.Thread(target=cal_cube, args=(arr,))
th1.start()
th2.start()
th1.join()
th2.join()
print('Total time taken by thread is :', time.time() - t1)   # print the total time