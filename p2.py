x=[1,2,3,4,5,6]
reverse=[]
for i in range(len(x)-1,-1,-1):
    reverse.append(x[i])
print(reverse)

x=[1,2,3,4,5]
n=len(x)
for i in range(n//2):
    x[i],x[n-1-i]=x[n-1-i],x[i]
print(x)