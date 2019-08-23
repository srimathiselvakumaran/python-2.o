n=int(input()) 
l=[int(x) for x in input().split()]  
for i in range(1,n-1):
  a=l.count(i)
  if(a>=2):
    print(i,end=' ')
  
