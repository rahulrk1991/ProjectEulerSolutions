def inc(n):
  flag,x=0,10
  while n!=0 :
    y=n%10
    if y>x:
      flag=1
      break
    else :
      x=y
    n=n/10
  return flag

def dec(n):
  flag,x=0,0
  while n!=0 :
    y=n%10
    if y<x:
      flag=1
      break
    else :
      x=y
    n=n/10
  return flag  

print inc(232),dec(232)
b=0  
for i in range(1,10000000):
  if (inc(i)) & (dec(i)) :
    b=b+1
  r=float(b)/i
  if r==0.99 :
    print i
    break
print i,' ',r
