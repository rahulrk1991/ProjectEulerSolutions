f=open('matrix.txt','r')
a=[]
for i in range(80):
  x=(f.readline())
  x=x.split(',')
  for j in range(80):
    x[j]=int(x[j])
  a.append(x)
print len(a),a[79]
