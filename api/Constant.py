from mpi4py import MPI
from mpi4py.MPI import Datatype


class Constant:
    MPI_INT = 'i'
    MPI_FLOAT = 'f'
    MDS_DISTANCE_MATRIX_PATH= '/home/vibhatha/github/bio/data/distance_matrices/mds_distance.csv'
    DISTANCE_MATRIX_PATH = '/home/vibhatha/github/bio/data/distance_matrices/2400-gene-distance-matrix.csv'
    MDS_DISTANCE_MATRIX_MAT_PATH = '/home/vibhatha/Sandbox/bio/distance_matrices/mds_dis.mat'
    DISTANCE_MATRIX_MAT_PATH = '/home/vibhatha/Sandbox/bio/distance_matrices/real_dis.mat'

    def get_type(self, mpi_type=MPI.INT):
        if(mpi_type == MPI.INT):
            return self.MPI_INT
        if(mpi_type == MPI.FLOAT):
            return self.MPI_FLOAT

