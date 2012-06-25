def reverse(m):
  n=0
  while m!=0:
    n=(n*10)+(m%10)
    m=m/10
  return n

def prepare(n):
  flag,i,a=1,1,[]
  while flag :
    x=n*i
    x=reverse(x)
    while x!=0 :
      if (x%10==0) :
        return 0
      a.append(x%10)
      x=x/10
    i=i+1
    if len(a)==9 :
      return a
    elif len(a)>9 :
      return 0

for i in range(1,10000):
  z=prepare(i)
  k=0
  if z :
    d=set(z)
    if len(z)==len(d) :
      f=0
      for i in range(0,9):
        f=f*10+z[i]
      if f>k :
        k=f
        print k
