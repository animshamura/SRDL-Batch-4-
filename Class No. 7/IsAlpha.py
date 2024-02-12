def IsAlpha(c):
    return c.isalpha()

s = input("Enter the main string : ")
for i in s: 
    if(IsAlpha(i)): print(i,"is an alphabet!")
    else: print(i,"is not an alphabet!")
