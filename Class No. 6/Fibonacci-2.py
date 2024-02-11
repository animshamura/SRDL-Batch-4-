def Fibo(n):  
    if(n<=1): return n+1
    else: 
        f = 0
        s = 1
        t = 1
        c = 2
        while(t<n):
            t = f + s
            f = s   
            s = t
            c+=1
    return c
n = int(input())    
print(n,"is",Fibo(n),"th term!")   