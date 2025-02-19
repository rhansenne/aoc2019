# play & solve manually :)
from day09 import intcode
ic=[int(x) for x in open('input.txt', 'r').readline().split(',')]+[0 for x in range(100000)]

inp=[]
while True:
    res=intcode.execute(ic,inp)
    print(chr(res),end='')
    if res==ord('?'):
        inp=[ord(c) for c in input(' >')]+[10]