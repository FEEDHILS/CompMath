import numpy as np

# Метод монотонной прогонки (Алгоритм Томаса)

testmatrix = np.matrix("8 8 0 0 0 0 0 0 0; 7 4 -3 0 0 0 0 0 0; 0 10 6 -4 0 0 0 0 0; 0 0 7 3 -10 0 0 0 0; 0 0 0 -5 0 5 0 0 0; 0 0 0 0 8 3 -5 0 0; 0 0 0 0 0 -6 2 4 0; 0 0 0 0 0 0 -2 12 -10; 0 0 0 0 0 0 0 18 -13")
testd = np.array([3, 1, 2, 9, 6, 2, 4, 1, 2 + 3/2])


# Данный алгоритм лучше и проще реализовывать не с матрицей, а с тремя векторами (которые вдоль диагонали).
# Мне впадлу
def ThomasAlgo(matrix : np.matrix, d):
    matrix_dim = matrix.shape[0] # Предполагая что она квадратная (Не думаю что иначе метод вообще работает)
    a, b, x = [], [], []

    a.append(-matrix[0,1] / matrix[0,0])
    b.append(d[0] / matrix[0,0])

    for i in range(1, matrix_dim-1):
        a.append( -matrix[ i, i+1 ] / ( matrix[i, i] + matrix[i, i-1]*a[i-1] ) )
        b.append( (d[i] - matrix[i, i-1]*b[i-1]) / ( matrix[i, i] + matrix[i, i-1]*a[i-1] ) )

    x.append( (d[-1] - matrix[-1,-2]*b[-1])/(matrix[-1,-1] + matrix[-1,-2]*a[-1]) )

    for i in range(matrix_dim - 2, -1, -1):
        x.append( a[i]*x[-1] + b[i] )
    
    x.reverse()

    return np.array( x )


if __name__ == '__main__':
    res = ThomasAlgo(testmatrix, testd)
    print(res)
    print( testmatrix * res )
