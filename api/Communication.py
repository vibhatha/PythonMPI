from mpi4py import MPI


class Communication:
    mpi = MPI
    comm = MPI.COMM_WORLD
    size = comm.Get_size()

    def __init__(self):
        rank = self.comm.Get_rank()
        if (rank == 0):
            print("Initial Configurations : World Size = " + str(self.size))

    def send(self, input=[], dest=1, tag=1):
        self.comm.isend(input, dest=dest, tag=tag)

    def recv(self, source=1, tag=1, type=MPI.INT):
        data = self.comm.irecv(source=source, tag=tag)
        return data

