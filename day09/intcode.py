relbase=i=offset=0

def reset():
    global i,relbase,offset
    relbase=i=offset=0

def execute(ic,input=None):
    global i,relbase,offset
    a=b=idx_in=0
    while(True):
        instr=ic[i] % 100
        #determine mode
        if instr != 3:
            match (ic[i] // 10**2 % 10):
                case 0:
                    a=ic[ic[i+1]]
                case 1:
                    a=ic[i+1]
                case 2:
                    a=ic[relbase+ic[i+1]]
            match (ic[i] // 10**3 % 10):
                case 0:
                    b=ic[ic[i+2]]
                case 1:
                    b=ic[i+2]
                case 2:
                    b=ic[relbase+ic[i+2]]
            offset=0
            if (ic[i] // 10**4 % 10) == 2:
                offset=relbase
        else:        
            if (ic[i] // 10**2 % 10) == 2:
                offset=relbase
        #execute instruction
        match instr:
            case 1:
                ic[offset+ic[i+3]]=a+b
                i+=4
            case 2:
                ic[offset+ic[i+3]]=a*b
                i+=4
            case 3:
                ic[offset+ic[i+1]]=input[idx_in]
                i+=2
                idx_in+=1
            case 4:
                i+=2
                return a
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
                    ic[offset+ic[i+3]]=1
                else:
                    ic[offset+ic[i+3]]=0
                i+=4            
            case 8:
                if a==b:
                    ic[offset+ic[i+3]]=1
                else:
                    ic[offset+ic[i+3]]=0
                i+=4            
            case 9:
                relbase+=a
                i+=2
            case 99:
                break