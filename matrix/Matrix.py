import numpy as np

class Matrix:
    rows = 0
    columns = 0
    dtype = 'i'
    def init_matrix(self, rows=1, columns=1, dtype=int):
        data = np.empty(shape=[rows,columns], dtype=dtype)
        matrix = np.matrix(data, dtype=dtype, copy=True)
        return matrix
