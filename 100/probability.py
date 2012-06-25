from math import sqrt
i=1000000000000
while 1 :
  x = (1+sqrt(float(1)+2*(i*(i-1))))/2
  if (x-int(x)) == 0 :
    print i,x
    break
  i=i+1
print x-int(x)
