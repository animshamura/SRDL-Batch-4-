fileread = open('filereadwrite.txt','r')
content = fileread.readlines()
filewrite = open('filewriteread.txt','a')
for line in content:
         filewrite.write(line)
    