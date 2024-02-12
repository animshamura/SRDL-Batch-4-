s = input("Enter a sentence : ")
# Item Access 
print("Printing character accessing characters directly!")
for i in s: print(i,end=" ")
print()
print("Printing character using Indices!")
for i in range(len(s)): print(s[i],end=" ")

