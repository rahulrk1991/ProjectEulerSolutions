a,b=[],[]
n=5
for i in range(n):
  a.append(0)
for i in range(n):
  b[i].append(a)
for i in range(n):
  for j in range(n):
    if (i==j) :
      print i,j,i==j
      b[i][j]=1
      
print b[0]
