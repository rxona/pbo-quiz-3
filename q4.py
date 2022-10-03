a = [
     [5, 3], 
     [3, 4]
    ]
b = [
     [6, 3],
     [7, 3]
    ]
c = [
     [5, 4],
     [12, 10],
     [9, 17]
    ]

def getColumn(matrix, i):
  column = []
  for j in range(len(matrix)):
    column.append(matrix[j][i])

  return column

def subtract(matrixA, matrixB):
  r = range(len(matrixA))
  result = matrixA.copy()
  for i in r:
    for j in r:
      result[i][j] -= matrixB[i][j]
  return result;

def divide(matrixA, matrixB):
  return 'Matrix cannot be divided'

def multiple(matrixA, matrixB):
  ordo = {"a": [len(matrixA), len(matrixA[0])], "b": [len(matrixB), len(matrixB[0])]}
  if ordo["a"][1] != ordo["b"][0]:
    return 'Matrix cannot be multiplied because n columns A != n rows B'
  result = []
  for mx in matrixA:
    row = []
    for i in range(ordo["a"][0]):
      sum = 0
      for j in range(ordo["a"][1]):
        sum += mx[j] * getColumn(matrixB, i)[j]
      row.append(sum)
    result.append(row)
  return result


print('A x B = ', multiple(a, b))
print('A - B = ', subtract(a, b))
print('A x C = ', multiple(a, c))
print('B x C = ', multiple(b, c))
print('B / A = ', divide(a, b))