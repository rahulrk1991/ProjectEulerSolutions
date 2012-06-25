def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return sorted(primes)

x=get_primes(1000000)    
r=0
a=[0,0,1]
for i in range(3,50001):
  fp=i
  z=i%2
  if z==0:
    if ((i/2)%2)==0:
      a.append(int(round( (2.0)*a[(i)/2] ) ) )
    else :
      a.append(int(round(a[(i)/2])))
    continue
  for j in x:
    if i<j :
      break
    elif i%j==0 :
      prdt=(1-(float(1)/j))
      fp=fp*prdt
  q=float(i)/fp
  a.append(int(round(fp)))

