a = int(input("Enter first value : "))
b = int(input("Enter second value : "))
#Amar iccha hoise tai baad disi
square1 = a**2 + 2*a*b + b**2
square2 = a**2 - 2*a*b + b**2
cube1 = a**3 + 3*(a**2)*b + 3*a*(b**2) + b**3
cube2 = a**3 - 3*(a**2)*b + 3*a*(b**2) - b**3
#Amar iccha hoise tai baad disi
print(f"(a+b)^2 of {a} and {b} is",square1)
print(f"(a-b)^2 of {a} and {b} is",square2)
print(f"(a+b)^3 of {a} and {b} is",cube1)
print(f"(a-b)^3 of {a} and {b} is",cube2)


