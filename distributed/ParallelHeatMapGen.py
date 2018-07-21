import sys

sys.path.append('/home/vibhatha/github/bio/PythonMPI')
from matrix import Matrix
from api import Constant
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns;

sns.set()
import time
from comms import Communication


class ParallelHeatMapGen:
    def initialize(self, grid_size = 10):
        struct = {}
        #print("Initializing ...")

        realMat, mdsMat = self.load_matrices()
        # gen.pair_distances(realMat=[[1,2,3,4,5],[1,2,3,4,5]][0], mdsMat=[[5,4,3,2,1],[5,4,3,2,1]][0])
        pointsX, pointsY = self.pair_distances(realMat=realMat, mdsMat=mdsMat)
        minVal, maxVal = self.get_min_max(matrixA=realMat, matrixB=mdsMat)
        step = (maxVal - minVal) / grid_size
        return minVal, maxVal, pointsX, pointsY, step

    def __init__(self, real_mat, mds_mat):
        self.real_mat = real_mat
        self.mds_mat = mds_mat

    def load_matrices(self):
        #print("Real Mat : " + self.real_mat)
        #print("MDS Mat : " + self.mds_mat)
        matrix = Matrix.Matrix()
        mds_dis_mat_struct = matrix.load_matrix(filepath=matrix.mds_mat)
        mds_dist_mat = mds_dis_mat_struct['distance_matrix']

        matrix = Matrix.Matrix()
        real_dis_mat_struct = matrix.load_matrix(filepath=matrix.real_mat)
        real_dist_mat = real_dis_mat_struct['distance_matrix']
        return real_dist_mat, mds_dist_mat

    def pair_distances(self, realMat, mdsMat):
        rows = realMat.shape[0]
        pointsX = []
        pointsY = []
        for row in range(0, rows, 1):
            for x, y in zip(realMat[row], mdsMat[row]):
                pointsX.append(x)
                pointsY.append(y)
        return np.array(pointsX), np.array(pointsY)

    def getRowByRow(self, matrix):
        [rows, columns] = matrix.shape
        print(matrix[0])

    def get_min_max(self, matrixA, matrixB):
        matA_max = np.max(matrixA)
        matB_max = np.max(matrixB)

        matA_min = np.min(matrixA)
        matB_min = np.min(matrixB)
        minVal = min(matA_min, matB_min)
        maxVal = max(matA_max, matB_max)
        return minVal, maxVal

    def gen_grid(self, minVal=0, maxVal=1, step=0.01):
        x_grid_list = []
        for val in np.arange(minVal, maxVal, step):
            x_grid_list.append(val)
        return np.array(x_grid_list, dtype=np.float64)

    def bcast_grid(self, x_grid_list, y_grid_list, comms=None):
        comms.bcast(input=x_grid_list, dtype=comms.mpi.FLOAT, root=0)
        comms.bcast(input=y_grid_list, dtype=comms.mpi.FLOAT, root=0)

    def scatter_data(self, pointsX, pointsY, num_of_data_per_rank=1, comms=None):
        recvbufX = np.empty(num_of_data_per_rank, dtype=np.float64)
        recvbufY = np.empty(num_of_data_per_rank, dtype=np.float64)
        comms.scatter(input=pointsX, recvbuf=recvbufX, dtype=comms.mpi.FLOAT, root=0)
        comms.scatter(input=pointsY, recvbuf=recvbufY, dtype=comms.mpi.FLOAT, root=0)
        return recvbufX, recvbufY

    def gen_heatmap(self,pointsX=[], pointsY=[], step=0.006, minVal=0, maxVal=1000, box_size=3):
        box = np.zeros((box_size*box_size), dtype=int)
        x_grid_list = []

        for val in np.arange(minVal, maxVal, step):
            x_grid_list.append(val)

        y_grid_list = x_grid_list
        box_index=0
        for y_grid_index in range(0, len(y_grid_list), 1):
            for x_grid_index in range(0, len(x_grid_list),1):
                for x_val, y_val in zip(pointsX, pointsY):
                    x_low = x_grid_list[x_grid_index]
                    y_low = y_grid_list[y_grid_index]
                    x_high = x_low + step
                    y_high = y_low + step
                #print(str(x_low) + " < " + str(x_val) + "< " + str(x_high))
                #print(str(y_low) + " < " + str(y_val) + "< " + str(y_high))
                    if ((x_low <= x_val and x_val <= x_high) and (y_low <= y_val and y_val <= y_high)):
                        #recurrence_count = 0
                        #pointsX, pointsY, recurrence_count =self.remove_iterated_occurences(box_index, pointsX, x_val, pointsY, y_val)
                        box[box_index] += 1
                        #box[box_index] += recurrence_count
                print("Box Count : ", box[box_index])
                box_index = box_index + 1

        return box


    def get_heatmap_grid(self, box_in, box_out, comms=None):
        comms.reduce(input=box_in, output=box_out, op=comms.mpi.SUM, dtype=comms.mpi.INT, root=0)


exec_time = 0
exec_time -= time.time()
grid_size = 10
comms = Communication.Communication()
rank = comms.comm.Get_rank()
size = comms.comm.Get_size()

const = Constant.Constant()
para = ParallelHeatMapGen(real_mat=const.DISTANCE_MATRIX_MAT_PATH, mds_mat=const.MDS_DISTANCE_MATRIX_MAT_PATH)
minVal, maxVal, pointsX, pointsY, step = para.initialize(grid_size=grid_size)
#print("Old Points Shape ", pointsY.shape)
num_of_data_per_rank = len(pointsX) / size
box_size = grid_size
box_out = np.zeros((box_size * box_size), dtype=int)

if(rank == 0):
    x_grid_list = y_grid_list = para.gen_grid(minVal=minVal, maxVal=maxVal, step=step)
    box_in = np.zeros((box_size * box_size), dtype=int)
    print(str(box_out))

else:
    x_grid_list = np.zeros(grid_size, dtype=np.float64)
    y_grid_list = np.zeros(grid_size, dtype=np.float64)
    recvbufX = np.empty(num_of_data_per_rank, dtype=np.float64)
    recvbufY = np.empty(num_of_data_per_rank, dtype=np.float64)



para.bcast_grid(x_grid_list=x_grid_list, y_grid_list=y_grid_list, comms=comms)


recvbufX, recvbufY=para.scatter_data(pointsX=pointsX, pointsY=pointsY, num_of_data_per_rank=num_of_data_per_rank, comms=comms)

box_in = para.gen_heatmap(pointsX=recvbufX, pointsY=recvbufY, step=step, minVal=minVal, maxVal=maxVal, box_size=box_size)

print("Rank", rank, len(x_grid_list), len(y_grid_list))
print("Rank", rank, len(recvbufX), len(recvbufY) )

para.get_heatmap_grid(box_in=box_in, box_out=box_out, comms=comms)

if (rank == 0):
    print(str(box_out))
    print(np.sum(box_out))
    heat_grid = np.reshape(box_out, newshape=(grid_size,grid_size))
    ax = sns.heatmap(heat_grid, annot=True, fmt="d")

    plt.show()

exec_time += time.time()
print("Total Execution Time : " + str(exec_time) +" s")
