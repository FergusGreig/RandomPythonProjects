# problem is whats the maximum x for which x^2 + (x+1)^2+...+ (x+n)2 can equal 2002;
# 
import math
print( 'start')
test = 2002
xmax = round(math.sqrt(test))
sumsq = 0
for x in range(1,xmax):
    for i in range(x,xmax):
        sumsq = sumsq+(i^2)
        if sumsq == 2002:
            print(x, "works")
        elif sumsq < 2002:
            print(x, "doesn't work")
            sumsq = 0
            break
print('end')