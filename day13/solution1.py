from day09 import intcode
ic=[int(x) for x in open('input.txt', 'r').readline().split(',')]+[0 for x in range(1000)]

ptr=blocks=0
while True:
    res=intcode.execute(ic)
    if res==None:
        break
    if ptr%3==2 and res==2:
        blocks+=1
    ptr+=1
print(blocks)