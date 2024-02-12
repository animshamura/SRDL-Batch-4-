def Count(a,b):
    return a.count(b)

a = input("Enter the main string : ")
b = input("Entrer the substring : ")
print("The occurence of",b,"in",a,"is",Count(a,b))