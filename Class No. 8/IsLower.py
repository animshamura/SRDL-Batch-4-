def IsLower(s): 
    return s.islower()

s = input("Enter the main string : ")
if(IsLower(s)): print("'",s,"' is in lower case!")
else: print("'",s,"' is not in lower case!")