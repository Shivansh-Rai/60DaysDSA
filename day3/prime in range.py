a,b=map(int,input().split())
def isprime(num):
    status=False
    for i in range(2,int(num**0.5)):
        if num%i==0:
            status=False
            continue
        else:
            status=True
    return status
l=[]
for i in range(a,b+1):
    if isprime(i)==True:
        l.append(i)
print(l)   
    