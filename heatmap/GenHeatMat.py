import sys
sys.path.append('/home/vibhatha/github/bio/PythonMPI')
from matrix import Matrix
from api import Constant
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns; sns.set()
import time

class GenHeatMap:

    def __init__(self, real_mat, mds_mat):
        self.real_mat = real_mat
        self.mds_mat = mds_mat

    def load_matrices(self):
        print("Real Mat : " + self.real_mat)
        print("MDS Mat : " + self.mds_mat)
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

    def remove_iterated_occurences(self, index, pointsX, x_val, pointsY, y_val):
        pointsX_avail_index = np.where(pointsX == x_val)
        pointsY_avail_index = np.where(pointsY == y_val)
        #print(index,len(pointsX_avail_index))
        #print(index,len(pointsY_avail_index))
        common_indexes = np.intersect1d(pointsX_avail_index, pointsY_avail_index)
        #print("Remove Count",index,len(common_indexes))
        pointsX = np.delete(pointsX, common_indexes)
        pointsY = np.delete(pointsY, common_indexes)
        return pointsX, pointsY, len(common_indexes)


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



const = Constant.Constant()
gen = GenHeatMap(real_mat=const.DISTANCE_MATRIX_MAT_PATH, mds_mat=const.MDS_DISTANCE_MATRIX_MAT_PATH)
realMat, mdsMat = gen.load_matrices()
#gen.pair_distances(realMat=[[1,2,3,4,5],[1,2,3,4,5]][0], mdsMat=[[5,4,3,2,1],[5,4,3,2,1]][0])
print(realMat.shape)

pointsX, pointsY = gen.pair_distances(realMat=realMat, mdsMat=mdsMat)

print(len(pointsX), len(pointsX))

minVal, maxVal = gen.get_min_max(matrixA=realMat, matrixB=mdsMat)

grid_size = 15

step = (maxVal - minVal) / grid_size

intensity = np.arange(minVal, maxVal, step)

print(minVal, maxVal)





exec_time = 0
exec_time -= time.time()
box = gen.gen_heatmap(pointsX=pointsX, pointsY=pointsY, step=step, minVal=minVal, maxVal=maxVal, box_size=grid_size)
exec_time += time.time()
print(box)

sum = np.sum(box)
print("Total Points: ",sum)
print("Exec Time : " + str(exec_time) + "s")
heat_grid = np.reshape(box, newshape=(grid_size,grid_size))
ax = sns.heatmap(heat_grid, annot=True, fmt="d")

plt.show()

#plt.savefig('figures/'+str(grid_size)+"X"+str(grid_size)+".png")
