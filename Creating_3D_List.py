# Creation and handling 3D list

n=int(input("Enter the number of rows: "))
m=int(input("Enter the number of columns: "))
p=int(input("Enter the third dimension: "))

a=[]
a=[[[input() for i in range(p)] for j in range(n)] for k in range(m)]

print(a)
