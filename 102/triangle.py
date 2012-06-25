def power(x1,y1,x2,y2,x3,y3):
  m = (((y3-y1)*(x2-x1))-((y2-y1)*(x3-x1)))
  n = (((x1-x2)*y1)+(x1*(y2-y1)))
  if ((m<0) & (n<0)) | ((m>0) & (n>0)) :
    return 1
  else :
    return 0

f=open('triangle.txt','r')
a=[]
cnt=0
for i in range(1001):
  b=f.readline()
  a=b.split(',')
  for j in range(len(a)):
    a[j]=int(a[j])
  if (power(a[0],a[1],a[2],a[3],a[4],a[5])) & (power(a[4],a[5],a[2],a[3],a[0],a[1])) & (power(a[0],a[1],a[4],a[5],a[2],a[3])) :
    cnt=cnt+1
  a=[]
print cnt
