import random, networkx as nx
from day09 import intcode

ic=[int(x) for x in open('input.txt', 'r').readline().split(',')]+[0 for x in range(1000)]
co=[0,0]
G = nx.Graph()
while True:
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
        break
print(len(nx.shortest_path(G, (0,0),tuple(co2)))-1)
    