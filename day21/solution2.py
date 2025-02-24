from day09 import intcode
ic=[int(x) for x in open('input.txt', 'r').readline().split(',')]+[0 for x in range(100000)]
command=[ord(c) for c in "NOT B T\nNOT C J\nOR T J\nAND D J\nAND H J\nNOT A T\nOR T J\nRUN\n"]
print(command)
while True:
    res=intcode.execute(ic,command)
    if res==None:
        break
    if res<=256:
        print(chr(res),end='')
    else:
        print(res)