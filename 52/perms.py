import itertools

def strip(n):
  y=0
  i=n
  while i!=0 :
    y=y*10+(i%10)
    i=i/10
  x=()
  while y!=0 :
    x=x+((y%10),)
    y=y/10
  return x
  
for i in range(10,1000000):
  a= strip(i)
  perm=(set(itertools.permutations(a)))
  if (strip(2*i) in perm) & (strip(3*i) in perm) & (strip(4*i) in perm) & (strip(5*i) in perm) & (strip(6*i) in perm) :
    print i
  
