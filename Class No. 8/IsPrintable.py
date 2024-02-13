def IsPrintable(s):
    return s.isprintable()

s = input("Enter the main string :")
if(IsPrintable(s)): print("'",s,"' is printable!")
else: print("'",s,"' is not printable!")