import itertools

def get_output(input1,input2):
    ic=[int(x) for x in open('input.txt', 'r').readline().split(',')]
    a=b=i=0
    phase_done=False
    while(True):
        instr=ic[i] % 100
        if instr in [1,2,5,6,7,8]:
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
                if not phase_done:
                    ic[ic[i+1]]=input1
                    phase_done=True
                else:
                    ic[ic[i+1]]=input2
                i+=2
            case 4:
                return ic[ic[i+1]]
            case 5:
                if a!=0:
                    i=b
                else:
                    i+=3
            case 6:
                if a==0:
                    i=b
                else:
                    i+=3
            case 7:
                if a<b:
                    ic[ic[i+3]]=1
                else:
                    ic[ic[i+3]]=0
                i+=4            
            case 8:
                if a==b:
                    ic[ic[i+3]]=1
                else:
                    ic[ic[i+3]]=0
                i+=4            
            
def get_signal(seq):
    output=0
    for phase in seq:
        output=get_output(phase,output)
    return output
            
print(max([get_signal(setting) for setting in itertools.permutations([0,1,2,3,4])]))