def Triangle(n,c): 
    for i in range(1,n+1):
        for j in range(1,i+1):
            if(i==1 or i==n or j==1 or j==i): print(c,end=" ")
            else: print(" ",end=" ")
        print()

n = int(input("Enter the length of the triangle: "))
c = input("Enter the character - the triangle will be filled with: ")
Triangle(n,c)  
