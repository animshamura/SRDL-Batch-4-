def Square(n,c): 
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(i==1 or i==n): print(c,end=" ")
            elif(j ==1 or j==n or j==i or j== n-i):
                     print(c,end=" ")
            else: print(" ",end=" ")
        print()

n = int(input("Enter the length of the square: "))
c = input("Enter the character - the square will filled with: ")
Square(n,c)