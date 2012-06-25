x=[]
f=open('input.txt','r')
str1=f.read()
l=str1.split('\n')
for i in range((len(l)-1)):
  s=l[i]
  t=s.split(' ')
  temp=[]
  for j in range(len(t)):
    y=int(t[j])
    temp.append(y)
  x.append(temp)
print x

k=len(x)-2
while k!=-1:
  j=len(x[k])
  for i in range(j):
    if (x[j][i])>(x[j][i+1]) :
      x[j-1][i]=x[j-1][i]+x[j][i]
    else:
      x[j-1][i]=x[j-1][i]+x[j][i+1]
  k=k-1  
print x[0][0]
