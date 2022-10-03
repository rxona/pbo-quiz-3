def add(matrixA, matrixB):
  result = []
  for i in range(len(matrixA)):
    row = []
    for j in range(len(matrixA[0])):
      row.append(matrixA[i][j] + matrixB[i][j])
    result.append(row)
  return result

def subtract(matrixA, matrixB):
  r = range(len(matrixA))
  result = matrixA.copy()
  for i in r:
    for j in r:
      result[i][j] -= matrixB[i][j]
  return result
  
a = [
     [2, 3], 
     [4, 5]
    ]
b = [
     [4, 6],
     [8, 2]
    ]

def getColumn(matrix, i):
  column = []
  for j in range(len(matrix)):
    column.append(matrix[j][i])

  return column

print('A + B = ', add(a, b))
print('A - B = ', subtract(a, b))