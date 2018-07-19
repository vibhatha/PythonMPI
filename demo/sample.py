from mpi4py import MPI


class Initial:
    comm = []
    rank = 0

    def __init__(self):
        comm = MPI.COMM_WORLD
        rank = comm.Get_rank()

        if rank == 0:
            data = {'a': 7, 'b': 3.14}
            comm.isend(data, dest=1, tag=11)
            print("Sending : " + str(data) + ": Rank " + str(rank))
        elif rank == 1:
            data = comm.irecv(source=0, tag=11)
            print("Receiving : " + str(data) + ": Rank " + str(rank))


init = Initial()
