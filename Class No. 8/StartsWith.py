def StartsWith(s,k):
    return s.startswith(k)
    
s = input("Enter the main string : ")
k = input("Enter the query string : ")
if(StartsWith(s,k)): print(s,'starts with',k)
else: print(s,"doesn't start with",k)