def factors(number):
  a= [x for x in range(1, number/2 + 1) if number % x == 0 ] + [number]
  s=0
  for i in range(len(a)-1):
    s=s+a[i]
  return s
x=[]
for i in range(1,28124):
  if factors(i)>i:
    x.append(i)

y=[]
for i in range(len(x)):
  for j in range(len(x)):
    y.append(x[i]+x[j])
    
y=list(set(y))
y.sort()
z=[]
for i in range(len(y)):
  if y[i]<28124:
    z.append(y[i])
print z[0:12],len(z)
a=[]
for i in range(1,28124):
  a.append(i)
for i in range(len(z)):
  a.remove(z[i])
print len(a)
s=0
for i in range(len(a)):
  s=s+a[i]
print s  
