def IsTitle(s):
    return s.istitle()

s = input("Enter the main string : ")
if(IsTitle(s)): print("'",s,"' is a title!")
else: print("'",s,"' is not a title!")

