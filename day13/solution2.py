from day09 import intcode
ic=[int(x) for x in open('input.txt', 'r').readline().split(',')]+[0 for x in range(100000)]
ic[0]=2
input=[0]
paddle_x=ball_x=score=0
while True:
    res=[intcode.execute(ic,input),intcode.execute(ic,input),intcode.execute(ic,input)]
    if res[0]==None:
        break #game ended
    if res[2]==3:
        paddle_x=res[0]
    if res[2]==4:
        ball_x=res[0]
        if paddle_x<ball_x:
            input=[1]
        elif paddle_x>ball_x:
            input=[-1]
        else:
            input=[0]
    if res[:-1]==[-1,0]:
        score=res[2]
print(score)