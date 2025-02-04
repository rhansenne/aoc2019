from day09 import intcode
ic=[int(x) for x in open('input.txt', 'r').readline().split(',')]+[0 for x in range(100000)]

view=[[]]
while True:
    res=intcode.execute(ic)
    if res==10:
        view.append([])
    elif res==46:
        view[-1].append('.')
    elif res==35:
        view[-1].append('#')
    elif res==None:
        break
view=view[:-2]

tot=i=j=0
for i in range(1,len(view)-1):
    for j in range(1,len(view[i])-1):
        if view[i][j]==view[i-1][j]==view[i+1][j]==view[i][j-1]==view[i][j+1]=="#":
            tot+=i*j
print(tot)