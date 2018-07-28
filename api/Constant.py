from mpi4py import MPI
from mpi4py.MPI import Datatype


class Constant:
    MPI_INT = 'i'
    MPI_FLOAT = 'f'
    MDS_DISTANCE_MATRIX_PATH= '/home/vibhatha/github/bio/data/distance_matrices/mds_distance.csv'
    MDS_9556_DISTANCE_MATRIX_PATH = '/home/vibhatha/Sandbox/bio/distance_matrices/mds_9556_distance.csv'
    DISTANCE_MATRIX_PATH = '/home/vibhatha/github/bio/data/distance_matrices/2400-gene-distance-matrix.csv'
    DISTANCE_MATRIX_9556_PATH = '/home/vibhatha/Sandbox/bio/distance_matrices/distance-matrix-9556.csv'
    DISTANCE_MATRIX_9556_MAT_PATH = '/home/vibhatha/Sandbox/bio/distance_matrices/real_9556.mat'
    MDS_DISTANCE_MATRIX_MAT_PATH = '/home/vibhatha/Sandbox/bio/distance_matrices/mds_dis.mat'
    MDS_9556_DISTANCE_MATRIX_MAT_PATH = '/home/vibhatha/Sandbox/bio/distance_matrices/mds_9556_dis.mat'
    DISTANCE_MATRIX_MAT_PATH = '/home/vibhatha/Sandbox/bio/distance_matrices/real_dis.mat'
    DAMDS_OUTPUT_POINTS_PATH = '/home/vibhatha/github/dsc-spidal-forks/applications/fungi-gene-sequence/scripts/damds/damds-points-9556.txt'#"/Users/bfeng/DSC-SPIDAL/applications/fungi-gene-sequence/scripts/damds/damds-points.txt.formatted"
    DAMDS_2_CSV_OUTPUT_PATH = "/home/vibhatha/Sandbox/bio/distance_matrices/mds_9556_distance.csv"

    def get_type(self, mpi_type=MPI.INT):
        if(mpi_type == MPI.INT):
            return self.MPI_INT
        if(mpi_type == MPI.FLOAT):
            return self.MPI_FLOAT

