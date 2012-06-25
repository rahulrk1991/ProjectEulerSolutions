import itertools

def isprime(n):
   if n == 2: return True
   if n == 3: return True
   if n % 2 == 0: return False
   if n % 3 == 0: return False

   i = 5
   w = 2
   while i * i <= n:
      if n % i == 0:
         return False

      i += w
      w = 6 - w

   return True

a=(7,6,5,4,3,2,1)   
perm=list(itertools.permutations(a))
for i in range(0,len(perm)):
  x=0
  y=perm[i]
  for j in range(7):
    x=x*10+y[j]
  if isprime(x):
    print x
    break
