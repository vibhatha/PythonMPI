import scipy.io as sio
import numpy as np
import time

class LoadMatrix:

    mat_path = '/home/vibhatha/Sandbox/bio/distance_matrices/dis.mat'

    def load_matrix(self):
        return sio.loadmat(self.mat_path)

exec_time = 0
exec_time -= time.time()
loadMatrix = LoadMatrix()
disMat_struct = loadMatrix.load_matrix()
exec_time += time.time()
print(disMat_struct)
disMat = disMat_struct['distance_matrix']
print(disMat.shape)
print("Execution Time : " + str(exec_time) + " s")
