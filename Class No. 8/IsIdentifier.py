def IsIdentifier(s):
    return s.isidentifier()

s = input("Enter the main string :")
if(IsIdentifier(s)): print(s,'is an identifier!')
else:  print(s,'is not an identifier!')