s,p=0,0
for i in range(1,1000,2):
  a,x,b=[],10,[]
  for j in range(2000):
    y=x/i
    a.append(y)
    b.append(x%i)
    if y==0:
      x=x*10
      continue
    else :
      x=(x%i)*10  
  if s<len(set(b)) :
    s = len(set(b))
    p=i
    print p,s

