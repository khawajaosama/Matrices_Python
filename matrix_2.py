#Making Of a Matrix

def make_matrix(no_rows,no_col):
    return [[functios(no_col_i,no_rows_i)
             for no_col_i in range(no_col)]
                for no_rows_i in range(no_rows)
                ]

def functios(no_col_i,no_rows_i):
    return 1 if no_rows_i==no_col_i else 0


print(make_matrix(3,3))