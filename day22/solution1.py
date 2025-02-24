size=10007
deck=[i for i in range(size)]
for t in open('input.txt', 'r').readlines():
    if "deal into new stack" in t:
        deck.reverse()
    elif "cut" in t:
        cut=int(t[4:])
        deck=deck[cut:]+deck[:cut]
    elif "deal with increment" in t:
        inc=int(t[20:])
        new=[0]*size
        for i in range(size):
            new[i*inc%size]=deck[i]
        deck=new
print(deck.index(2019))