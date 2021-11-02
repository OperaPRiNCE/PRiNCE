def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
num=int(input("Enter fast number="))
if num<0:
    print("Enter positive number")
else:
    print("Result=",factorial(num))
    
