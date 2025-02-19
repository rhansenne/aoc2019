import sys, numpy as np
from day09 import intcode
ic=[int(x) for x in open('input.txt', 'r').readline().split(',')]+[0 for x in range(30000)]

size=2000
sq=np.zeros((size,size), dtype=int)
for i in range(size):
    for j in range(size):
        sq[i][j]=intcode.execute(ic.copy(),[i,j])
        intcode.reset()

s=100
for i in range(size-s):
    for j in range(size-s):
        if np.all(sq[i:i+s,j:j+s]):
            print(i*10000+j)
            sys.exit(0)