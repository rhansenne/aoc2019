import copy
startgrid=[[*l.strip()] for l in open('input.txt', 'r').readlines()]
emptygrid=[['.' for i in range(5)] for j in range(5)]
grids={0:startgrid,-1:copy.deepcopy(emptygrid),1:copy.deepcopy(emptygrid)} #grids per depth
gridsnew={}
            
def get_grid(depth):
    if not depth in grids.keys():
        gn=copy.deepcopy(emptygrid)
        gridsnew[depth]=gn
        return gn
    return grids[depth]

def bug(depth,i,j):
    return 1 if get_grid(depth)[i][j]=='#' else 0

def bugs():
    tot=0
    for grid in grids.values():
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]=='#':
                    tot+=1
    return tot            

def update_grid(depth):
    grid=grids[depth]
    grid2=copy.deepcopy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i,j)==(2,2):
                continue
            a=0
            if (i,j)==(0,0):
                a+=bug(depth-1,1,2)+bug(depth-1,2,1)+bug(depth,0,1)+bug(depth,1,0)
            elif (i,j)==(0,4):
                a+=bug(depth-1,1,2)+bug(depth-1,2,3)+bug(depth,0,3)+bug(depth,1,4)
            elif i==0:
                a+=bug(depth-1,1,2)+bug(depth,0,j-1)+bug(depth,0,j+1)+bug(depth,1,j)
            elif (i,j)==(4,0):
                a+=bug(depth-1,3,2)+bug(depth-1,2,1)+bug(depth,4,1)+bug(depth,3,0)
            elif (i,j)==(4,4):
                a+=bug(depth-1,3,2)+bug(depth-1,2,3)+bug(depth,4,3)+bug(depth,3,4)
            elif i==4:
                a+=bug(depth-1,3,2)+bug(depth,4,j-1)+bug(depth,4,j+1)+bug(depth,3,j)
            elif j==0:
                a+=bug(depth-1,2,1)+bug(depth,i-1,j)+bug(depth,i+1,j)+bug(depth,i,j+1)
            elif j==4:
                a+=bug(depth-1,2,3)+bug(depth,i-1,j)+bug(depth,i+1,j)+bug(depth,i,j-1)
            elif (i,j)==(1,2):
                a+=bug(depth,0,2)+bug(depth,1,1)+bug(depth,1,3)+bug(depth+1,0,0)+bug(depth+1,0,1)+bug(depth+1,0,2)+bug(depth+1,0,3)+bug(depth+1,0,4)
            elif (i,j)==(3,2):
                a+=bug(depth,4,2)+bug(depth,3,1)+bug(depth,3,3)+bug(depth+1,4,0)+bug(depth+1,4,1)+bug(depth+1,4,2)+bug(depth+1,4,3)+bug(depth+1,4,4)
            elif (i,j)==(2,1):
                a+=bug(depth,2,0)+bug(depth,1,1)+bug(depth,3,1)+bug(depth+1,0,0)+bug(depth+1,1,0)+bug(depth+1,2,0)+bug(depth+1,3,0)+bug(depth+1,4,0)
            elif (i,j)==(2,3):
                a+=bug(depth,2,4)+bug(depth,1,3)+bug(depth,3,3)+bug(depth+1,0,4)+bug(depth+1,1,4)+bug(depth+1,2,4)+bug(depth+1,3,4)+bug(depth+1,4,4)
            else:
                a+=bug(depth,i-1,j)+bug(depth,i+1,j)+bug(depth,i,j-1)+bug(depth,i,j+1)
            if grid[i][j]=='#' and a!=1:
                grid2[i][j]='.'
            elif grid[i][j]=='.' and a in (1,2):
                grid2[i][j]='#'                    
    gridsnew[depth]=grid2

for i in range(200):
    gridsnew=copy.deepcopy(grids)
    for d in grids.keys():
        update_grid(d)
    grids=gridsnew    
print(bugs())