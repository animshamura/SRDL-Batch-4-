def Fibo(n):  
    if(n<=2): return n-1
    else: 
        f = 0
        s = 1
        global t
        for i in range(3,n+1):
            t = f + s
            f = s
            s = t
    return t
n = int(input())    
print(n,"th term is",Fibo(n))