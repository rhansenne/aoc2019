import re, math

vel=[]
pos=[]
repeat_freq=[]
initial_pos=[] # initial 10 positions
hist_pos=[] # 10 last historical positions
for l in open('input.txt', 'r').readlines():
    res = re.search(r'x=(-?\d+), y=(-?\d+), z=(-?\d+)',l)
    pos.append([int(res.group(1)),int(res.group(2)),int(res.group(3))])
    vel.append([0,0,0])
    repeat_freq.append([0,0,0])
    hist_pos.append([[],[],[]])
    initial_pos.append([[],[],[]])

freqs=[]
step=0
while True:
    for p1 in range(4):
        for i in range(3):
            if step<10: # look for repeating coordinates based on last 10 changes
                initial_pos[p1][i].append(pos[p1][i])
                hist_pos[p1][i].append(0)
            else:
                if repeat_freq[p1][i]==0:
                    hist_pos[p1][i].pop(0)
                    hist_pos[p1][i].append(pos[p1][i])
                    if hist_pos[p1][i]==initial_pos[p1][i]:
                        repeat_freq[p1][i]=step-9
                        freqs.append(step-9)
    if len(freqs)==12:
        break
    for p1 in range(4):
        for p2 in range(p1+1,4):
            for i in range(3):
                if pos[p1][i]>pos[p2][i]:
                    vel[p1][i]-=1
                    vel[p2][i]+=1
                elif pos[p1][i]<pos[p2][i]:
                    vel[p1][i]+=1                
                    vel[p2][i]-=1                
        for i in range(3):
            pos[p1][i]+=vel[p1][i]  
    step+=1

print(math.lcm(*freqs))