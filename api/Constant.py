from mpi4py import MPI
from mpi4py.MPI import Datatype


class Constant:
    MPI_INT = 'i'
    MPI_FLOAT = 'f'
    DISTANCE_MATRIX_PATH='/home/vibhatha/github/bio/data/distance_matrices/mds_distance.csv'

    def get_type(self, mpi_type=MPI.INT):
        if(mpi_type == MPI.INT):
            return self.MPI_INT
        if(mpi_type == MPI.FLOAT):
            return self.MPI_FLOAT

