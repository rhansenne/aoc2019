from shapely.geometry import LineString

def get_segments(path):
    segments=[]
    co1=co2=(0,0)
    for p in path:
        match p[0]:
            case 'R':
                co2=(co1[0]+int(p[1:]),co1[1])
            case 'L':
                co2=(co1[0]-int(p[1:]),co1[1])
            case 'U':
                co2=(co1[0],co1[1]+int(p[1:]))
            case 'D':
                co2=(co1[0],co1[1]-int(p[1:]))
        segments.append(LineString([co1,co2]))
        co1=co2
    return segments

def dist(p1,p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

paths=[l.strip().split(',') for l in open('input.txt', 'r').readlines()]
path1=get_segments(paths[0])
path2=get_segments(paths[1])

steps=[]
dist1=0
for s1 in path1:
    dist2=0
    for s2 in path2:
        ints = s1.intersection(s2)
        if ints:
            steps.append(dist1+dist2+dist((ints.x,ints.y),s1.coords[0])+dist((ints.x,ints.y),s2.coords[0]))
        dist2+=s2.length
    dist1+=s1.length
print(min(steps[1:]))