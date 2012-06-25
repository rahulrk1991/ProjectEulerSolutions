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

a=7
flag=1
while flag:
  while isprime(a+2):
    a=a+2
  a=a+2
  for i in range(1,a):
    x=a-(2*i*i)
    if (x>0) & (isprime(x)):
      break
    elif (x<0) :
      print a
      flag=0
      break
