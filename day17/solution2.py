from day09 import intcode
import collections
ic=[int(x) for x in open('input.txt', 'r').readline().split(',')]+[0 for x in range(100000)]

# execute intcode to determine map
pos=[0,0]
view=[[]]
x=y=0
while True:
    res=intcode.execute(ic)
    if res==10:
        view.append([])
        x+=1
    elif res==46:
        view[-1].append('.')
        y+=1
    elif res==35:
        view[-1].append('#')
        y+=1
    elif res==None:
        break
    else:
        view[-1].append(chr(res))
        pos=[x,y]
view=view[:-2]
    
# determine path as instruction list -> can certainly be refactored to get rid of repeating code
instr=''
fwd=0
while True:
    if view[pos[0]][pos[1]]=='^':
        if pos[0]>0 and view[pos[0]-1][pos[1]]=='#':
            view[pos[0]][pos[1]]='#'
            pos[0]-=1
            view[pos[0]][pos[1]]='^'
            fwd+=1
        elif pos[1]>0 and view[pos[0]][pos[1]-1]=='#':
            view[pos[0]][pos[1]]='<'
            if fwd>0:
                instr+=str(fwd)+','
            instr+='L,'
            fwd=0
        elif pos[1]<len(view[0])-1 and view[pos[0]][pos[1]+1]=='#':
            view[pos[0]][pos[1]]='>'
            if fwd>0:
                instr+=str(fwd)+','
            instr+='R,'
            fwd=0
        else:
            instr+=str(fwd)
            break
    elif view[pos[0]][pos[1]]=='>':
        if pos[1]<len(view[0])-1 and view[pos[0]][pos[1]+1]=='#':
            view[pos[0]][pos[1]]='#'
            pos[1]+=1
            view[pos[0]][pos[1]]='>'
            fwd+=1
        elif pos[0]>0 and view[pos[0]-1][pos[1]]=='#':
            view[pos[0]][pos[1]]='^'
            if fwd>0:
                instr+=str(fwd)+','
            instr+='L,'
            fwd=0
        elif pos[0]<len(view)-1 and view[pos[0]+1][pos[1]]=='#':
            view[pos[0]][pos[1]]='v'
            if fwd>0:
                instr+=str(fwd)+','
            instr+='R,'
            fwd=0
        else:
            instr+=str(fwd)
            break
    elif view[pos[0]][pos[1]]=='v':
        if pos[0]<len(view)-1 and view[pos[0]+1][pos[1]]=='#':
            view[pos[0]][pos[1]]='#'
            pos[0]+=1
            view[pos[0]][pos[1]]='v'            
            fwd+=1
        elif pos[1]<len(view[0])-1 and view[pos[0]][pos[1]+1]=='#':
            view[pos[0]][pos[1]]='>'
            if fwd>0:
                instr+=str(fwd)+','
            instr+='L,'
            fwd=0
        elif pos[1]>0 and view[pos[0]][pos[1]-1]=='#':
            view[pos[0]][pos[1]]='<'
            if fwd>0:
                instr+=str(fwd)+','
            instr+='R,'
            fwd=0        
        else:
            instr+=str(fwd)
            break
    if view[pos[0]][pos[1]]=='<':
        if pos[1]>0 and view[pos[0]][pos[1]-1]=='#':
            view[pos[0]][pos[1]]='#'
            pos[1]-=1
            view[pos[0]][pos[1]]='<'            
            fwd+=1
        elif pos[0]<len(view)-1 and view[pos[0]+1][pos[1]]=='#':
            view[pos[0]][pos[1]]='v'
            if fwd>0:
                instr+=str(fwd)+','
            instr+='L,'
            fwd=0        
        elif pos[0]>0 and view[pos[0]-1][pos[1]]=='#':
            view[pos[0]][pos[1]]='^'
            if fwd>0:
                instr+=str(fwd)+','
            instr+='R,'
            fwd=0
        else:
            instr+=str(fwd)
            break   

#find repeating substrings in instruction list
#https://stackoverflow.com/questions/49222636/finding-repeated-character-combinations-in-string
lrss={}
min_length=3
prev=''
substrings = (
    instr[i:i+j]
    for i in range(0, len(instr) - min_length + 1)
    for j in range(min_length, len(instr) - i + 1)
)
counts = collections.Counter(substrings)
ss=list(filter(lambda key: counts[key] > 2, counts))

# find the 3 repeating substrings that compress the instruction list the most
for i in range(3):
    mf=chr(ord('A')+i)
    shortest=len(instr)
    best=''
    for substring in ss:
        substring=substring.strip(',')
        l=len(instr.replace(substring,mf))
        if l<shortest and len(substring)<=20:
            shortest=l
            best=substring
    lrss[mf]=best
    instr=instr.replace(best,mf)

# create ascii instructions
args=[instr+'\n']
for k, v in lrss.items():
    args.append(v+'\n')
args.append('n\n')
args_ascii=[[ord(c) for c in s] for s in args]
    
# execute intcode with instructions
ic=[int(x) for x in open('input.txt', 'r').readline().split(',')]+[0 for x in range(100000)]
ic[0]=2    
intcode.reset()
i=0
prev_res=0
while True:
    res=intcode.execute(ic,args_ascii[i])
    if res==None:
        print(prev_res) # print the result
        break
    elif res==99: #provide next input
        i+=1
    prev_res=res