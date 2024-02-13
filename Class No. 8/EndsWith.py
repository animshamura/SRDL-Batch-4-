def EndsWith(s,k):
    return s.endswith(k)

s = input("Enter the main string : ")
k = input("Enter the query string : ")
if(EndsWith(s,k)): print(s,'ends with',k)
else: print(s,"doesn't end with",k)