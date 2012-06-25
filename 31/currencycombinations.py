cnt=0
for i in range(201):
  for j in range(101):
    x=i*1+j*2
    if x>200:
      break
    for k in range(41):
      x=i*1+j*2+k*5
      if x>200:
        break
      for l in range(21):
        x=i*1+j*2+k*5+l*10
        if x>200:
          break
        for m in range(11):
          x=i*1+j*2+k*5+l*10+m*20
          if x>200:
            break
          for n in range(5):
            x=i*1+j*2+k*5+l*10+m*20+n*50
            if x>200:
              break
            for o in range(3):
              x=i*1+j*2+k*5+l*10+m*20+n*50+o*100
              if x>200:
                break
              for p in range(2):
                x=(i*1+j*2+k*5+l*10+m*20+n*50+o*100+p*200)
                if x==200:
                  cnt=cnt+1
                  print cnt,i
                  x=0
print cnt
