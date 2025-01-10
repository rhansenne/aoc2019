ic=[int(x) for x in open('input.txt', 'r').readline().split(',')]
a=b=i=0
while(True):
    instr=ic[i] % 100
    if instr in [1,2]:
        if ic[i] // 10**2 % 10 == 0:
            a=ic[ic[i+1]]
        else:
            a=ic[i+1]
        if ic[i] // 10**3 % 10 == 0:
            b=ic[ic[i+2]]
        else:
            b=ic[i+2]
    match instr:
        case 1:
            ic[ic[i+3]]=a+b
            i+=4
        case 2:
            ic[ic[i+3]]=a*b
            i+=4
        case 3:
            ic[ic[i+1]]=1
            i+=2
        case 4:
            print(ic[ic[i+1]])
            i+=2
        case 99:
            break