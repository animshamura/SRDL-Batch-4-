file = open('filereadadvanced.txt','r')
lines = file.readlines()
for line in lines : print(line,end="")
file.close()    