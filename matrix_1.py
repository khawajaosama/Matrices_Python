# FIND ROW AND COULMN OF A MATRIX

A=[
    [2,3,4],
    [6,3,5]
]

def total_rows(matrix):
    return len(matrix)

print(total_rows(A))



def find_row(matrix,row_no):
    return matrix[row_no-1]

print(find_row(A,2))



def total_col(matrix):
    return len(matrix[0])

print(total_col(A))



def find_col(matrix,col_no):
    return [row_no_i[col_no-1]
             for row_no_i in matrix]

print(find_col(A,2))
