import intcode
ic=[int(x) for x in open('input.txt', 'r').readline().split(',')]+[0 for x in range(1000000)]
print(intcode.execute(ic,[1]))