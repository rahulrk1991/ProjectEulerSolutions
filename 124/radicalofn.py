def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes
    
a=sorted(list(get_primes(1000000)))
b=[(1,1)]

for i in range(2,100001):
  x = i
  j,prdt = 0,1
  while x!=1 :
    flag=0
    while x%a[j]==0 :
      x=x/a[j]
      flag=1
    j=j+1
    if flag :
      prdt=prdt*a[j-1]
  tup = (i, prdt)
  b.append(tup)

def rad(y) :
  return y[1]

b=sorted(b,key=rad)
print b[10000-1]
