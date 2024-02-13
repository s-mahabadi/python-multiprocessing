from multiprocessing import Process, Lock

def f(l, i):
    # l.acquire()
    try:
        print('hello world', i)
    finally:
        pass
        # l.release()

if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        Process(target=f, args=(lock, num)).start()


# The output of the program is not guaranteed to be in any particular order.

# A sample output of the program is shown below:
# >> python .\example_processes_sync_standard_output_nolock.py
# hello world 0
# hello world 1
# hello world 2
# hello world 3
# hello world 4
# hello world 6
# hello world 8
# hello world 5
# hello world 9
# hello world 7