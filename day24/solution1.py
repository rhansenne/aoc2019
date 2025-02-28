import copy
grid = [[*l.strip()] for l in open('input.txt', 'r').readlines()]

def adj(i,j):
    a=0
    if i>0 and grid[i-1][j]=='#':
        a+=1
    if i<len(grid)-1 and grid[i+1][j]=='#':
        a+=1
    if j>0 and grid[i][j-1]=='#':
        a+=1
    if j<len(grid[i])-1 and grid[i][j+1]=='#':
        a+=1
    return a

history=[]
while True:
    grid2=copy.deepcopy(grid)
    rating=0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            a=adj(i,j)
            if grid[i][j]=='#' and a!=1:
                grid2[i][j]='.'
            elif grid[i][j]=='.' and a in (1,2):
                grid2[i][j]='#'
            if grid2[i][j]=='#':
                rating+=pow(2,i*len(grid[0])+j)    
    #print(grid)
    #print(grid2)
    if grid2 in history:
        print(rating)
        break
    grid=grid2
    history.append(grid)