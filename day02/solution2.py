ico = [int(x) for x in open('input.txt', 'r').readline().split(',')]
for i in range(100):
    for j in range(100):
        ic = ico.copy()
        ic[1]=i
        ic[2]=j
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
        if ic[0] == 19690720:
            print(100*i+j)
            exit(0)