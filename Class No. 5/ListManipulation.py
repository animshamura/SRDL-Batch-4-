FriendList = [] # Define a list! 
for i in range(10):
    name = input()
    FriendList.append(name) # Append in the list!
print(FriendList) # Print the list!

#Access item
idx = int(input("Enter item to access within 0 - 9 :"))    
print('Required name is ',FriendList[idx])

FriendList[3] = "Shifa"
print(FriendList)
NumberList = [1,2,3,4,4,4,6,7,8,9,10]
print(NumberList)
NumberList.remove(8)
print(NumberList)
print(NumberList.count(4))             

