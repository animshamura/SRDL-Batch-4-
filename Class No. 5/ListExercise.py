name = [] 
for i in range(15):
    n = input()
    name.append(n)

marks = []
for i in range(15):
    m = int(input())
    marks.append(m)

result = [] 
for i in range(15): 
     if(marks[i]>=33): result.append(True)
     else: result.append(False)

for i in range(15): 
    print(name[i],"got",marks[i],"! Did he/she pass? :",result[i])
 