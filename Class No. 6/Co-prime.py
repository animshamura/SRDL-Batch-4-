def Coprime(n1,n2): 
    ret = "are Co-primes!"
    n3 = min(n1,n2)
    for i in range(2,n3):
        if(n1%i==0 and n2%i==0): ret="are not Co-primes!"
    return ret

n1 = int(input())
n2 = int(input())
print(n1,"and",n2,Coprime(n1,n2))