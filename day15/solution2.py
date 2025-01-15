import random, networkx as nx
from day09 import intcode

ic=[int(x) for x in open('input.txt', 'r').readline().split(',')]+[0 for x in range(1000)]
co=[0,0]
co_ox=None
G = nx.Graph()
for i in range(10000000): # brute force scan of environment via random moves
    mv=random.randint(1,4)
    res=intcode.execute(ic,[mv])
    if res>0:
        co2=co.copy()
        match(mv):
            case 1:
                co2[1]-=1
            case 2:
                co2[1]+=1
            case 3:
                co2[0]-=1
            case 4:
                co2[0]+=1
        G.add_edge(tuple(co),tuple(co2))
        co=co2
    if res==2:
        co_ox=tuple(co2)

longest=0
for dest in G.nodes: #find longest shortest path
    if dest!=co_ox:
        longest=max(longest, len(nx.shortest_path(G,co_ox,dest))-1)
print(longest)