b,a=[],[]
n=40
for i in range(n):
  a.append(b)
  for j in range(i+1):
    a[i].append(b)
    a[i][j]=0
  b=[]
print "done"
def euclid(numA, numB):
  m,n=numA,numB
  while numB != 0:
    numRem = numA % numB
    numA = numB
    numB = numRem
    if numB==0:
      a[m-1][n-1]=numA
      return
    if a[numA-1][numB-1] :
      a[m-1][n-1]=a[numA-1][numB-1]
      return

for i in range(n):
  for j in range(i+1):
    euclid(i+1,j+1)

for i in range(n):
  for j in range(i+1):
    print a[i][j],
  print
