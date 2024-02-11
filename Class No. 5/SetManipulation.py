A = {'Afif','Asif','Sakib'}
B = {'Asif','Ami','Jarif'}
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.pop())
A.remove('Asif')
print(A)
A.discard("Hasib")      
print(A)
A.add('Rafi')
print(A)
A.update('Tayef','Rafi')
print(A)