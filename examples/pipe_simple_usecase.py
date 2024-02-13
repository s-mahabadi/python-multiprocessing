from multiprocessing import Pipe
a, b = Pipe()

# either one of a or b can be used to send data to the other end of the pipe

a.send([1, 'hello', None])
print("b.recv() = ", b.recv())

b.send_bytes(b'thank you')
print("a.recv_bytes() = ", a.recv_bytes())

import array
arr1 = array.array('i', range(5))
arr2 = array.array('i', [0] * 10)
a.send_bytes(arr1)
count = b.recv_bytes_into(arr2)
print(f"count ({count}) == len(arr1) * arr1.itemsize ({len(arr1) * arr1.itemsize})", count == len(arr1) * arr1.itemsize)
assert count == len(arr1) * arr1.itemsize
print(arr2)