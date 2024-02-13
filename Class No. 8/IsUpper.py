def IsUpper(s):
    return s.isupper()

s = input("Enter the main the string: ")
if(IsUpper(s)): print(s,'is in uppercase!')
else: print("'",s,"' is not in uppercase!")