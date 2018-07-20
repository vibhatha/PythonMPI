import sys
sys.path.append('/home/vibhatha/github/bio/PythonMPI')
from matrix import Matrix

class MatrixImpl:
    matrix = Matrix.Matrix()
    def gen_matrix(self):
        rows = 3
        columns = 3
        matA = self.matrix.init_matrix(rows=rows, columns=columns, dtype=int)
        print(matA)
matrixImpl = MatrixImpl()
matrixImpl.gen_matrix()
