n=int(input())
k=int(input())

n1=str(n)
num=int(n1*k)

sum=0
while (num!=0):
    rem=num%10
    sum+=rem
    num//=10

while (sum>=10):
    temp=0
    while (sum>0):
        rem=sum%10
        temp+=rem
        sum=Sum // 10
    sum=temp

print(sum)