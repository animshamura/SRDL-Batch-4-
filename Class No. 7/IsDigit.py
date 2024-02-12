def IsDigit(c):
    return c.isdigit()

s = input("Enter the main string : ")
for i in s : 
    if(IsDigit(i)): print(i,'is a digit!')
    else: print(i,'is not a digit!')