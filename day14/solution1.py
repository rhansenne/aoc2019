import re,math
reactions={}
for l in open('input.txt', 'r').readlines():
    res = re.findall(r'((\d+ [A-Z]+[,]?[ ]?)+) => (\d+) ([A-Z]+)',l)
    ingredients={i[2]:int(i[1]) for i in re.findall(r'((\d+) ([A-Z]+)[,]?[ ]?)',res[0][0])}
    reactions[res[0][3]]=(int(res[0][2]),ingredients)

def dict_add(d,key,inc):
    if key in d:
        d[key]+=inc
    else:
        d[key]=inc
                
needed=reactions['FUEL'][1]
spare={}
ore=0
while len(needed)>0:
    needed_exp={}
    for n,q in needed.items():
        if n=='ORE':
            ore+=q
            continue
        if n in spare:
            if spare[n]>q:
                spare[n]-=q
                continue
            else:
                q-=spare[n]
                spare[n]=0
        r=reactions[n]
        times=math.ceil(q/r[0])
        if q%r[0]>0:
            dict_add(spare,n,r[0]-q%r[0])
        for n2,q2 in r[1].items():
            dict_add(needed_exp,n2,q2*times)
    needed=needed_exp
print(ore)