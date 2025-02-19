from day09 import intcode
ic=[int(x) for x in open('input.txt', 'r').readline().split(',')]+[0 for x in range(100000)]

tot=0
for i in range(50):
    for j in range(50):
        tot+=intcode.execute(ic.copy(),[i,j])
        intcode.reset()
print(tot)