matrix = [[1,2], [3,4]]
sum=[]
for x in matrix:
    add=0
    for y in x:
        add += y
    sum.append(add)
print(sum)