# Creating a nested list from the input
M = []
row = input()
while row:
    t = []
    for i in row.strip().split(' '):
        t.append(i)
    M.append(t)
    row = input()


# New nested list for the rotated matrix
M_ = []
for i in range(len(M[0])):
    M_.append([])
    for j in range(len(M)):
        M_[i].append(0)

# Transformation
## Transpose
for i in range(len(M)):
    for j in range(len(M[0])):
        M_[j][i] = M[i][j]

## Flipping the rows of the transposed matrix
M_ = M_[::-1]

# Printing Rotated Matrix
for i in range(len(M_)): 
    for j in range(len(M_[0])): 
        if j != len(M_[0])-1:
            print(M_[i][j], end=' ')
        else:
            print(M_[i][j], end='')
    print()
