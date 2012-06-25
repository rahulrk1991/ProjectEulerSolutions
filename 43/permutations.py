import itertools
a=list(itertools.permutations([0,1,2,3,4,5,6,7,8,9]))

y=[]
z=[2,3,5,7,11,13,17]
w=[]
flag=0
for i in range(len(a)):
  x=a[i]
  for j in range(1,8):
    y.append(int(x[j]*100+x[j+1]*10+x[j+2]))
  for k in range(0,7):
    if ((y[k])%(z[k]))!=0 :
      flag=1
  if flag==0:
    w.append(x)
  flag=0
  y=[]
print w
