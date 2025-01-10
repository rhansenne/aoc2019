import networkx as nx
G = nx.Graph()
for orbit in [l.strip().split(')') for l in open('input.txt', 'r').readlines()]:
    G.add_edge(orbit[0],orbit[1])
print(len(nx.shortest_path(G, 'YOU', 'SAN'))-3)