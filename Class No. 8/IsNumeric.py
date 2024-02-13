def IsNumeric(s):
    return s.isnumeric()

s = input("Enter the main string :")
if(IsNumeric(s)): print(s,'is numeric!')
else: print(s,'is not numeric!')