import itertools
a=(1,2,3,4,5,6,7,8,9)
perm=list(itertools.permutations(a))

def factors(n):    
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def pandigital(m,n,p):
  b=()
  while m!=0 :
    b=b+(m%10,)
    if m%10 == 0:
      return [1,1]
      break
    m=m/10
  while n!=0 :
    b=b+(n%10,)
    if n%10 == 0:
      return [1,1]
      break
    n=n/10
  while p!=0 :
    b=b+(p%10,)
    if p%10 == 0:
      return [1,1]
      break
    p=p/10
  return b
  
cnt=0
for i in range(10,20000):
  x=sorted(list(factors(i)))
  for j in range((len(x)/2)):
    m=x[j]
    n=i/m
    a=pandigital(m,n,i)
    d=set(a)
    if (len(a)==9) & (len(d)==9) :
      print m,n,i
      cnt=cnt+i
      break
print cnt
