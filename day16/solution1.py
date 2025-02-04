pattern = [0, 1, 0, -1]
lst = [int(c) for c in open('input.txt', 'r').readline()]

def pat(i,j):
    return pattern[((j+1)//i)%len(pattern)]
    
for phase in range(100):
    lst2=[]
    for i in range(1,len(lst)+1):
        lst2.append(abs(sum(lst[j]*pat(i,j) for j in range(len(lst))))%10)
    lst=lst2
print(''.join(str(x) for x in lst[:8]))
        