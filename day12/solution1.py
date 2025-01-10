import re
vel=[]
pos=[]
for l in open('input.txt', 'r').readlines():
    res = re.search(r'x=(-?\d+), y=(-?\d+), z=(-?\d+)',l)
    pos.append([int(res.group(1)),int(res.group(2)),int(res.group(3))])
    vel.append([0,0,0])

for step in range(1000):
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

energy=0
for i in range(4):
    energy+=sum(abs(p) for p in pos[i])*sum(abs(v) for v in vel[i])
print(energy)