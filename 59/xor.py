f=open('cipher1.txt','r')
s=f.readline()
a=[]
a=s.split(',')
for i in range(len(a)):
  a[i]=(int(a[i]))
  print chr(a[i]),

