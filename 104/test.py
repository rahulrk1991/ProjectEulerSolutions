from math import sqrt

def main() :
  for i in range(200):
    z=((1+sqrt(5))**i-(1-sqrt(5))**i)/(2**i*sqrt(5))
    z=string(int(z))
    startlist(
  print i,z
  x,y=1,1
  for i in range(197) :
    z=x+y
    x=y
    y=z
  print i+3,z

if __name__ == '__main__' :
  main()
