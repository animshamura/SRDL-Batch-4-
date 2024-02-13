def IsDecimal(s): 
    return s.isdecimal()

s =  input("Enter the main string : ")
if(IsDecimal(s)): print("'",s,"' is a decimal number!")
else: print("'",s,"' is not a decimal number!")