import itertools

def naive(n):
    from itertools import count, islice
    primes = (n for n in count(2) if all(n % d for d in range(2, n)))
    return islice(primes, 0, n)

def isprime(n):
  n = abs(int(n))
  if n < 2:
    return False
  if n == 2:
    return True
  if not n & 1:
    return False
  for x in range(3, int(n**0.5)+1, 2):
    if n % x == 0:
      return False
  return True

def finder(a,b,c):
  p=strip(a)
  q=strip(b)
  r=strip(c)
  perm=list(itertools.permutations(p))
  if (q in perm) & (r in perm) :
    return 1
  else :
    return 0
    
def strip(n):
  z=()
  while n!=0 :
    z=z+(n%10,)
    n=n/10
  return z
    
a= list(naive(1500))
x=[]
for i in range(len(a)-1):
  if (a[i]>1000) & (a[i]<10000) :
    x.append(a[i])

print isprime(13)

for i in range(len(x)-2):
  for j in range(i+1,len(x)-1):
    a=x[i]
    b=x[j]
    d=b-a
    c=x[j]+d
    if (isprime(c)) :
      if finder(a,b,c) :
         print a,b,c
         
