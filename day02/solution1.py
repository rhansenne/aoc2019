ic = [int(x) for x in open('input.txt', 'r').readline().split(',')]
ic[1]=12
ic[2]=2
pos=0
while True:
    match ic[pos]:
        case 1:
            ic[ic[pos+3]]=ic[ic[pos+1]]+ic[ic[pos+2]]
        case 2:
            ic[ic[pos+3]]=ic[ic[pos+1]]*ic[ic[pos+2]]
        case 99:
            break
    pos+=4
print(ic[0])