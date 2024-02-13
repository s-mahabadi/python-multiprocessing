from multiprocessing import Process
import os

def f(name):
    print('hello', name)

if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    # p.join() # uncomment this line to see the difference
    while True:
        print('Process is running:', p.is_alive())
        if p.is_alive() == False:
            break
    print('Process is running:', p.is_alive())