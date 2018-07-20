import numpy as np
import scipy as sp
from scipy.spatial import distance_matrix

class Matrix:
    rows = 0
    columns = 0
    dtype = 'i'
    def init_matrix(self, rows=1, columns=1, dtype=int):
        data = np.empty(shape=[rows,columns], dtype=dtype)
        matrix = np.matrix(data, dtype=dtype, copy=True)
        return matrix


    def gen_distance_matrix(self,x, y, p=2, threashold=1000000):
        return distance_matrix(x=x, y=y, p=p , threshold=threashold)

    def get_matrix(self, array=np.empty(1)):
        matrix = np.matrix(array, copy=True)
        return matrix
