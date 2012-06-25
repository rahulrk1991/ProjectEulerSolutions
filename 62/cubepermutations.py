import itertools
cubelist=[]
for i in range(1,10000):
  cube=i*i*i
  a,b=(),()
  while cube!=0 :
    a=a+(cube%10,)
    cube=cube/10
  for i in range(len(a)):
    b=b+(a[-i-1],)
  cubelist.append(b)

perms=[]
for i in range(len(cubelist)):
  if i<5000:
    continue
  n=len(cubelist[i])
  j=1
  cnt=0
  perms = set(itertools.permutations(cubelist[i]))
  a=cubelist[i+j]
  
  while len(a)==n :
    a=cubelist[i+j]
    if a in perms :
      cnt=cnt+1
    j=j+1
  print i+1,cnt
  if cnt==4 :
    break
