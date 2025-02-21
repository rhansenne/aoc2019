mp = [[*c] for c in open('input.txt', 'r').readlines()]

# replace portals with single character
mapping={}
nxt='a'
portals=set()
def repl(port):
    global nxt, mapping
    if port not in mapping: 
        mapping[port]=nxt
        nxt=chr(ord(nxt)+1)
    return mapping[port]
          
for i in range(len(mp)):
    for j in range(len(mp[i])):
        if i<len(mp)-2 and 'A'<=mp[i][j]<='Z' and 'A'<=mp[i+1][j]<='Z' and mp[i+2][j]=='.': 
            mp[i+2][j]=repl(mp[i][j]+mp[i+1][j])
            portals.add((i+2,j))
            mp[i][j]=mp[i+1][j]=' '
        if i<len(mp)-2 and 'A'<=mp[i+1][j]<='Z' and 'A'<=mp[i+2][j]<='Z' and mp[i][j]=='.': 
            mp[i][j]=repl(mp[i+1][j]+mp[i+2][j])
            portals.add((i,j))
            mp[i+1][j]=mp[i+2][j]=' '
        if j<len(mp[i])-2 and 'A'<=mp[i][j]<='Z' and 'A'<=mp[i][j+1]<='Z' and mp[i][j+2]=='.': 
            mp[i][j+2]=repl(mp[i][j]+mp[i][j+1])
            portals.add((i,j+2))
            mp[i][j]=mp[i][j+1]=' '
        if j<len(mp[i])-2 and 'A'<=mp[i][j+1]<='Z' and 'A'<=mp[i][j+2]<='Z' and mp[i][j]=='.': 
            mp[i][j]=repl(mp[i][j+1]+mp[i][j+2])
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
        curr=mp[i][j]
        if (i,j)!=co and curr!='.':
            if not port in graph:
                graph[port]=set()
            addsymbol=True
            for (symbol,prevsteps) in graph[port].copy():
                if symbol==curr: 
                    if prevsteps>steps:
                        graph[port].remove((symbol,prevsteps))
                    else:
                        addsymbol=False
            if addsymbol:
                graph[port].add((curr,steps))
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
queue=[(mapping['AA'],0,set())]
while queue:
    (port,steps,visited) = queue.pop()   
    if port==mapping['ZZ']:
        minsteps=min(steps-1,minsteps)
        print("temp min steps", minsteps)
        continue
    visited.add(port)
    for (nxt,nxt_steps) in graph[port]:        
        if nxt in visited or steps+nxt_steps>=minsteps:
            continue        
        queue.append((nxt,steps+nxt_steps+1,visited.copy()))        
print(minsteps)