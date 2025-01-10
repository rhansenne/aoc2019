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

paths=[l.strip().split(',') for l in open('input.txt', 'r').readlines()]
path1=get_segments(paths[0])
path2=get_segments(paths[1])

l = [s1.intersection(s2) for s1 in path1 for s2 in path2]
l = filter(lambda x: not x.is_empty, l)
l = [abs(ints.x)+abs(ints.y) for ints in l]
print(min(l[1:]))