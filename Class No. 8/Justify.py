def LeftJustify(s,n):
    return s.ljust(n)

def RightJustify(s,n):
    return s.rjust(n)

s = input("Enter the main string : ")
n = int(input("Enter amount of justification : "))
print("Left justified :",LeftJustify(s,n))
print("Right justified :",RightJustify(s,n))

