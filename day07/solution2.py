import itertools
prog=[int(x) for x in open('input.txt', 'r').readline().split(',')]

def get_output(ic, i,input1,input2,phase_done):
    a=b=0
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
                return i+2,ic[ic[i+1]]
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
            case 99:
                return -1,-1
                
def get_signal(seq):
    output=0
    progs=[prog.copy() for p in range(5)]
    prog_pos=[0 for p in range(5)]
    phase_done=False    
    while True:
        for p in range(len(seq)):
            phase=seq[p]
            prog_pos[p],o=get_output(progs[p],prog_pos[p],phase,output,phase_done)
            if o==-1: #processing halted
                return output
            else:
                output=o
        phase_done=True
        
print(max([get_signal(setting) for setting in itertools.permutations([5,6,7,8,9])]))

get_signal([9,8,7,6,5])