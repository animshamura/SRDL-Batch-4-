def ZFill(s,n):
    return s.zfill(n)

s =  input("Enter main string :")
n = int(input("Enter adjusted length : "))
print("Before adding zeros :",s)
print("After adding zeros :",ZFill(s,n))

