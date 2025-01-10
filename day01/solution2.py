def fuel(m):
    f = m//3-2
    if f <= 0:
        return 0
    return f + fuel(f)

print(sum([(fuel(int(x))) for x in open('input.txt', 'r').readlines()]))