a=set()
for i in range(1,1000):
  for j in range(i+1,1000):
    a.add((i*1.0)/j)
a=list(a)
a.sort()    
x=a.index(3.0/7)
print a[x-1]
