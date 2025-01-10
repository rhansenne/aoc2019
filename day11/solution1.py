from day09 import intcode
facing=0 # 0=north, 1=east, 2=south, 3=west
ic=[int(x) for x in open('input.txt', 'r').readline().split(',')]+[0 for x in range(1000000)]

white=set()
painted=set()
co=(0,0)

while True:
    if co in white:
        currcolor=1
    else:
        currcolor=0
    paint=intcode.execute(ic,[currcolor])
    if paint==None:
        break
    if paint==1:
        white.add(co)
    elif co in white:
        white.remove(co)
    painted.add(co)
    turn=intcode.execute(ic,[])
    if turn==1:
        facing=(facing+1)%4
    else:
        facing=(facing-1)%4    
    match(facing):
        case 0:
            co=(co[0]-1,co[1])
        case 1:
            co=(co[0],co[1]+1)
        case 2:
            co=(co[0]+1,co[1])
        case 3:
            co=(co[0],co[1]-1)
print(len(painted))