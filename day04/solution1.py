def digit(number, n):
    return number // 10**n % 10

r=tuple(int(l) for l in open('input.txt', 'r').readline().split('-'))
met=0
for x in range(r[0],r[1]+1):
    adjsame=0
    valid=True
    for d in range(0,5):
        dr=digit(x,d)
        dl=digit(x,d+1)
        if dr==dl:
            adjsame+=1
        elif dr<dl:
            valid=False
    if valid and adjsame>0:
        met+=1
print(met)