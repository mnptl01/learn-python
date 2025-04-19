matrix=[[1,2], [3,4]]
transpose=[]
for i in range(len(matrix[0])):
    row=[]
    for j in range(len(matrix)):
        row.append(matrix[j][i])
    transpose.append(row)
print(transpose)

mat=[[1,2,3], [4,5,6]]
trn=[]
for i in range(len(mat[0])):
    rw=[]
    for j in range(len(mat)):
        rw.append(mat[j][i])
    trn.append(rw)
print(trn)
