for i in range(10,100):
  for j in range(i+1,100):
    if (j%10)!=0:
      if ( (i%10) == (j/10) ) & ( (float((i/10))/(j%10)) == (float(i)/j) ) :
        print i,'/',j
