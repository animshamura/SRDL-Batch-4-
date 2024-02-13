def IsAlNum(s):
    return s.isalnum()

s = input("Enter the main string : ")
if(IsAlNum(s)): print(s,"is alphanumeric!")
else: print(s,"is not alphanumeric!")