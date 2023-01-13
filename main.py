# nth Prime palindrome finder
n = int(input("Enter number:"))
flag = 0
for i in range(2,n):
    if n%i==0:
        flag=1
        print(i)
        break
if flag==1:
    print(n,"is not a prime")
else:
    print(n,"is prime")
    #palindrome check
    x=n
    sum =0
    while x>0:
        r=x%10
        sum=sum*10+r
        x=x//10
    if sum==n:
        print(n,"is a Prime Palindrome")
    else:
        print(n,"is not a Prime Palindrome")