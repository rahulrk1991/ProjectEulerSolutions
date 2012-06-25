a,c,d,e,f=[],[],[],[],[]
for i in range(1,1000):
    x=(i*((5*i)-3))/2
    if x <1000 :
      continue
    if x>10000:
      break
    a.append(str(x))

for i in range(1,1000):
    x=(i*(i+2))/2
    if x <1000 :
      continue
    if x>10000:
      break
    c.append(str(x))

for i in range(1,1000):
    x=i*i
    if x <1000 :
      continue
    if x>10000:
      break
    d.append(str(x))

for i in range(1,1000):
    x=i*((3*i-1))/2
    if x <1000 :
      continue
    if x>10000:
      break
    e.append(str(x))

for i in range(1,1000):
    x=i*(2*i-1)
    if x <1000 :
      continue
    if x>10000:
      break
    f.append(str(x))


def main():
  b=[]
  for i in range(1,1000):
    x=i*((3*i)-2)
    if x <1000 :
      continue
    if x>10000:
      break
    b.append(str(x))
  print f
  for s in b :
    for p in a :
      for r in c :
        for q in d :
          for t in e :
            if s[0:2]==p[2:4] and s[2:4]==r[0:2] and r[2:4]==q[0:2] and q[2:4]==t[0:2]:
              print p,s,r,q,t

  
if __name__ == '__main__' :
  main()
