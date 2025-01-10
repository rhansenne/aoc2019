w,h=25,6
pixels=[int(x) for x in open('input.txt', 'r').readline()]
image=[2 for x in range(w*h)]
for i in range(len(pixels)):
    x=i%(w*h)
    if image[x]==2:
        image[x]=pixels[i]
for i in range(h):
    for j in range(w):   
        match(image[i*w+j]):
            case 0:
                print(' ',end='')
            case 1:       
                print('\u2588',end='')
    print()