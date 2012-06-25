def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes
 
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
  
x,cnt=0,0    
a=get_primes(10000)
for i in range(2,len(a)+1):
  for j in range(len(a)-i+1):
    s=0
    for k in range(i):
      s=s+a[j+k]
    if (isprime(s)) & (i>cnt) & (s<1000000):
      x=s
      cnt=i
      print x,' ',cnt
