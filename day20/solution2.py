mp = [[*c] for c in open('input.txt', 'r').readlines()]
portals=set()

# replace portals with single character
mapping={}
coordinates={}
nxt='a'
def repl(co,port):
    global nxt, mapping
    if port not in mapping: 
        mapping[port]=nxt
        coordinates[nxt]={co}
        nxt=chr(ord(nxt)+1)
    else:
        coordinates[mapping[port]].add(co)
    return mapping[port]
          
for i in range(len(mp)):
    for j in range(len(mp[i])):
        if i<len(mp)-2 and 'A'<=mp[i][j]<='Z' and 'A'<=mp[i+1][j]<='Z' and mp[i+2][j]=='.': 
            mp[i+2][j]=repl((i+2,j),mp[i][j]+mp[i+1][j])
            portals.add((i+2,j))
            mp[i][j]=mp[i+1][j]=' '
        if i<len(mp)-2 and 'A'<=mp[i+1][j]<='Z' and 'A'<=mp[i+2][j]<='Z' and mp[i][j]=='.': 
            mp[i][j]=repl((i,j),mp[i+1][j]+mp[i+2][j])
            portals.add((i,j))
            mp[i+1][j]=mp[i+2][j]=' '
        if j<len(mp[i])-2 and 'A'<=mp[i][j]<='Z' and 'A'<=mp[i][j+1]<='Z' and mp[i][j+2]=='.': 
            mp[i][j+2]=repl((i,j+2),mp[i][j]+mp[i][j+1])
            portals.add((i,j+2))
            mp[i][j]=mp[i][j+1]=' '
        if j<len(mp[i])-2 and 'A'<=mp[i][j+1]<='Z' and 'A'<=mp[i][j+2]<='Z' and mp[i][j]=='.': 
            mp[i][j]=repl((i,j),mp[i][j+1]+mp[i][j+2])
            portals.add((i,j))
            mp[i][j+1]=mp[i][j+2]=' '

# build graph with number of steps between portals
graph={}
def build_graph(co):
    port=mp[co[0]][co[1]]
    visited=set()
    queue=[(co[0],co[1],0)]
    while queue:
        (i,j,steps) = queue.pop()
        curr=(mp[i][j],(i,j))
        if (i,j)!=co and curr[0]!='.':
            if not (port,co) in graph:
                graph[(port,co)]=set()
            addsymbol=True
            for (symbol,prevsteps) in graph[(port,co)].copy():
                if symbol==curr: 
                    if prevsteps>steps:
                        graph[(port,co)].remove((symbol,prevsteps))
                    else:
                        addsymbol=False
            if addsymbol:
                graph[(port,co)].add((curr,steps))
            continue
        steps+=1 
        visited.add((i,j))
        for dr in [(0,1),(1,0),(0,-1),(-1,0)]:
            i2,j2 = i+dr[0],j+dr[1]
            nxt = mp[i2][j2]
            if nxt in ('#',' ') or (i2,j2) in visited:
                continue        
            queue.append((i2,j2,steps))        

for p in portals:
    build_graph(p)
   
#determine shortest path   
minsteps=10000
queue=[((mapping['AA'],coordinates[mapping['AA']].pop()),0,0)]
while queue:
    (port,steps,lvl) = queue.pop()   
    for (nxt,nxt_steps) in graph[port]:
        if nxt[0]==mapping['AA'] or steps>=minsteps:
            continue        
        if nxt[0]==mapping['ZZ']:
            if lvl==0:
                minsteps=min(steps+nxt_steps,minsteps)
            continue
        #teleport
        nxtlvl=lvl
        if nxt[1][0]==2 or nxt[1][0]==len(mp)-3 or nxt[1][1]==2 or nxt[1][1]==len(mp[0])-4:
            nxtlvl-=1
        else:
            nxtlvl+=1      
        if lvl<0:
            continue
        for c in coordinates[nxt[0]]:
            if nxt[1]!=c:
                nxt=(nxt[0],c)
                break        
        queue.append((nxt,steps+nxt_steps+1,nxtlvl))        
print(minsteps)