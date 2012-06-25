

a,x,y=[],1,1
flag,flag2,flag3=1,1,1
i=2
while flag:
  n=x+y
  x=y
  y=n
  i=i+1
  print i,n
  if n<10000000000:
    continue
  while n!=0 :
    a.append(n%10)
    n=n/10
  b,c=[],[]
  d,e=set(),set()
  for j in range(9):
    if a[j]==0 :
      flag2=0
    b.append(a[j])
    if a[len(a)-j-1]==0 :
      flag3=0
    c.append(a[len(a)-j-1])
  if flag2  :
    d=set(b)
    e=set(c)
    if (len(b)==len(d))  :
      print i,b
      flag=0
  flag2,flag3=1,1
  if i==540:
     print b,d
     break
