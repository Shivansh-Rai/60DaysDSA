def isarm(num):
    n=str(num)
    l=len(n)
    s=0
    n1=num
    while (num!=0):
        rem=num%10
        s+=rem**l
        num=num//10
    if s==n1:
        return True
    else:
        return False

a=int(input())
b=int(input())
l=[]
for i in range(a,b+1):
    if isarm(i)==True:
        l.append(i)

if len(l)==0:
    print(-1)
else:
    for i in l:
        print(i,end=" ")