import sys
sys.path.append('/home/vibhatha/github/bio/PythonMPI')
from api import Constant
from api import FileRead
from matrix import Matrix
import scipy.io as sio
import time

class ReadBinFile:

    save_path = Constant.Constant().MDS_DISTANCE_MATRIX_MAT_PATH

    def read(self):
        filepath = Constant.Constant().MDS_DISTANCE_MATRIX_PATH
        fileReader = FileRead.FileRead()
        content = fileReader.read(filepath=filepath)
        length = fileReader.lenth(filepath=filepath)
        arr = fileReader.get_array_from_csv(filepath=filepath)
        return content, length, arr

    def get_distance_matrix(self):
        filepath = Constant.Constant().MDS_DISTANCE_MATRIX_PATH
        fileReader = FileRead.FileRead()
        arr = fileReader.get_array_from_csv(filepath=filepath)
        matrix = Matrix.Matrix()
        dis_mat = matrix.get_matrix(array=arr)
        return dis_mat

exec_time = 0
exec_time -= time.time()
readBinFile = ReadBinFile()
content, length, arr = readBinFile.read()
print(length)
print(arr.shape)
print("=======Load Matrix=========")

matrix = readBinFile.get_distance_matrix()
print(matrix.shape)
exec_time += time.time()
print("Execution Time For Loading Matrix via CSV : " + str(exec_time))
sio.savemat(readBinFile.save_path, {'distance_matrix':matrix} )

