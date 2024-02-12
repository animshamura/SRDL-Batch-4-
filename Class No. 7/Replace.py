def Replace(a,b,c): 
    return a.replace(b,c)

a = input("Enter the main string : ")
b = input("Enter the word to be replaced : ")
c = input("Enter the word to replace : ")
print("Before replacing :",a)
print("After replacing :",Replace(a,b,c))