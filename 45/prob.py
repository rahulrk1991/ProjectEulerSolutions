from math import sqrt
def Tn(x):
  n = (-1+sqrt(1+8*x))/2
  if n - int(n) == 0 :
    return 1
  else:
    return 0

def Pn(x):
  n = (1+sqrt(1+24*x))/6
  if n - int(n) == 0 :
    return 1
  else:
    return 0
    
for i in range(1,150000):
  Hi=(i*(2*i-1))
  if Tn(Hi) & Pn(Hi) :
    print Hi,' ',i

