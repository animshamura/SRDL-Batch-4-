list = ['Amir', 'Sorwar','Safi', 'Hasib','Topodar','Tanvir']
names = "\n".join(list)
file = open('filewriteadvanced.txt','w')
file.write(names)
file.close()