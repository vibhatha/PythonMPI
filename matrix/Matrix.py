import numpy as np
from scipy.spatial import distance_matrix
import scipy.io as sio
import time
from api import Constant


class Matrix:
    rows = 0
    columns = 0
    dtype = 'i'

    const = Constant.Constant()
    mds_mat = const.MDS_DISTANCE_MATRIX_MAT_PATH
    real_mat = const.DISTANCE_MATRIX_MAT_PATH

    def load_matrix(self, filepath=const.MDS_DISTANCE_MATRIX_MAT_PATH):
        return sio.loadmat(filepath)

    def init_matrix(self, rows=1, columns=1, dtype=int):
        data = np.empty(shape=[rows,columns], dtype=dtype)
        matrix = np.matrix(data, dtype=dtype, copy=True)
        return matrix


    def gen_distance_matrix(self,x, y, p=2, threashold=1000000):
        return distance_matrix(x=x, y=y, p=p , threshold=threashold)

    def get_matrix(self, array=np.empty(1)):
        matrix = np.matrix(array, copy=True)
        return matrix
