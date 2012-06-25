import math
j=2
s=0
sq=(1,4,9,16,25,36,49,64,81)
while j<100 :
  if j in sq:
    j=j+1
  a=[]
  k=int(math.log(j,2))
  q=2*(k)
  r= (j-(k*k))
  a.append(q/2)
  for i in range(99):
    q=q*10
    r=r*100
    x=9
    while ((q+x)*x) > r :
      x=x-1
    a.append(x)
    w=q+x+x
    v=r-((q+x)*x)
    q=w
    r=v
  print j,' ',sum(a)
  s=s+sum(a)
  j=j+1
print s
