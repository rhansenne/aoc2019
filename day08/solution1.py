w,h=25,6
pixels=[int(x) for x in open('input.txt', 'r').readline()]
minzeroes=len(pixels)
zeroes=ones=twoes=res=0
for i in range(len(pixels)):
    if i>0 and i%(w*h)==0:
        if zeroes<minzeroes:
            minzeroes=zeroes
            res=ones*twoes
        zeroes=ones=twoes=0
    if pixels[i]==0:
        zeroes+=1    
    elif pixels[i]==1:
        ones+=1    
    elif pixels[i]==2:
        twoes+=1    
print(res)