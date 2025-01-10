import networkx as nx
G = nx.DiGraph()
for orbit in [l.strip().split(')') for l in open('input.txt', 'r').readlines()]:
    G.add_edge(orbit[0],orbit[1])
sp = dict(nx.all_pairs_shortest_path(G))
print(sum([len(sp['COM'][planet])-1 for planet in G.nodes()]))