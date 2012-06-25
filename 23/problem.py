def factors(number):
  a= [x for x in range(1, number/2 + 1) if number % x == 0 ] + [number]
  s=0
  for i in range(len(a)-1):
    s=s+a[i]
  return s
a=0
p=0
h=0
s=0
def abundant(n):
  x=[]
  for i in range(1,n+1):
    num=factors(i)
    if num>i:
      a=a+1
    elif num==i:
      p=p+1
    else :
      h=h+1
  s=a+p+d
  print a,' ',p,' ',d,' ',s
      
abundant(28123)
y=[]
print "done1"
for i in range(len(x)):
  for j in range(len(x)):
    y.append(x[i]+x[j])
print "done2"
y=list(set(y))
y.sort()
z=[]
for i in range(len(y)):
  if y[i]<28124:
    z.append(y[i])
print "sorted",len(z)
s=0
for i in range(len(z)):
  s=s+z[i]
print s
