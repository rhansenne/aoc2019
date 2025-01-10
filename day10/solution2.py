import math

# https://manivannan-ai.medium.com/find-the-angle-between-three-points-from-2d-using-python-348c513e2cd
def angle(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang

def clockwise_angle_order(base, asteroid):
    ang = angle((-1,base[1]), base, asteroid)
    return -360 if ang == 0 else -ang

def distance(a,b):
  return math.sqrt((a[0]-b[0])**2+(a[0]-b[1])**2)

i=j=0
asteroids=[]
for l in open('input.txt', 'r').readlines():
    for c in l:
        if c=='#':
            asteroids.append((i,j))
        j+=1
    i+=1
    j=0

# find base
maxvisible=0
for a1 in asteroids:
    others=asteroids.copy()
    others.remove(a1)
    visible=0
    for i in range(len(others)):
        a2=others[i]
        isvisible=True        
        for j in range(0,i):
            a3=others[j]
            if angle(a2,a1,a3)==0:
                isvisible=False
        if isvisible:
            visible+=1
    if visible>maxvisible:
        maxvisible=visible
        base=a1

#vaporize asteroids based on angle and distance
asteroids.remove(base)
asteroids.sort(key=lambda x: ( clockwise_angle_order(base,x) , distance(base,x) ))
vaporized=0
while vaporized<200:
    prev_ang=-1
    for a in asteroids.copy():
        ang=angle((-1,base[1]),base,a)
        if ang == prev_ang: #hidden behind previous asteroid
            continue
        asteroids.remove(a) #vaporize a
        vaporized+=1
        if vaporized==200:
            print(a[1]*100+a[0])
        prev_ang=ang 