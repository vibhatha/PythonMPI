import sys
sys.path.append('/home/vibhatha/github/bio/PythonMPI')
import scipy.io as sio
import time
from api import Constant


class LoadMatrix:

    const = Constant.Constant()
    mds_mat = const.MDS_DISTANCE_MATRIX_MAT_PATH
    real_mat = const.DISTANCE_MATRIX_MAT_PATH

    def load_matrix(self, filepath=const.MDS_DISTANCE_MATRIX_MAT_PATH):
        return sio.loadmat(filepath)

exec_time = 0
exec_time -= time.time()
loadMatrix = LoadMatrix()
mds_dis_mat_struct = loadMatrix.load_matrix(filepath=loadMatrix.mds_mat)
exec_time += time.time()
print(mds_dis_mat_struct)
mds_dist_mat = mds_dis_mat_struct['distance_matrix']
print(mds_dist_mat.shape)
print("Execution Time : " + str(exec_time) + " s")


exec_time = 0
exec_time -= time.time()
loadMatrix = LoadMatrix()
real_dis_mat_struct = loadMatrix.load_matrix(filepath=loadMatrix.real_mat)
exec_time += time.time()
print(mds_dis_mat_struct)
real_dist_mat = real_dis_mat_struct['distance_matrix']
print(real_dist_mat.shape)
print("Execution Time : " + str(exec_time) + " s")
