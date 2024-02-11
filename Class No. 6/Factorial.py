def Fact(n):
    res = 1
    for i in range(2,n+1): res*=i
    return res

n = int(input())
print("Factorial of",n,"is :",Fact(n)) 
 