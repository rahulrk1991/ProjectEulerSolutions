f=open('matrix.txt','r')
a=[]
for i in range(80):
  x=(f.readline())
  x=x.split(',')
  for j in range(80):
    x[j]=int(x[j])
  a.append(x)
 
n=79
for i in range(1,n+1):
  for j in range(i+1):
    if j==0 :
      a[i][j]=a[i][j]+a[i-1][j]
    elif i==j:
      k=i-j
      a[k][j]=a[k][j]+a[k][j-1]
    else :
      k=i-j
      if a[k-1][j]>a[k][j-1] :
        a[k][j]=a[k][j]+a[k][j-1]
      else :
        a[k][j]=a[k][j]+a[k-1][j]

for i in range(n+1,2*n+1):
  for j in range(i-n,n+1):
    k=i-j
    if a[k-1][j]>a[k][j-1] :
      a[k][j]=a[k][j]+a[k][j-1]
    else :
      a[k][j]=a[k][j]+a[k-1][j]
print a
