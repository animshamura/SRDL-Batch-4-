def Prime(n):
    ret = "is Prime!"
    for i in range(2,n):
        if(n%i==0): ret ="is not Prime!"
    return ret

n = int(input())
print(n,Prime(n)) 