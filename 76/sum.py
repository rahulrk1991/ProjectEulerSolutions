a=[]
n=120000
for i in xrange(n):
  a.append([])
  for j in range(n):
    if i==j:
      a[i].append(1)
    else :
      a[i].append(0)
print 'done'
for i in range(0,n):
  j=i-1
  while j>=0 :
    a[i][j]=a[i][j+1]+a[i-j][j]
    j=j-1
  if ((a[i][0])%1000000)==0 :
    print i
    break
print a[i][0],i

