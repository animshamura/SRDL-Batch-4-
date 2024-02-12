def Find(s,c):
    return s.find(c)

s =  input("Enter the main string : ")
c = input("Enter the charcter to be found : ")
print('The occurence of ',c,'in',"'",s,"'","is",Find(s,c))
