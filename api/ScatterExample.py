import Communication
import numpy as np


class ScatterExample:
    comms = Communication.Communication()

    def example(self):
        rank = self.comms.comm.Get_rank()
        size = self.comms.comm.Get_size()
        num_of_data_per_rank = 2
        dt_size = range = size * num_of_data_per_rank
        input = np.linspace(1, range, dt_size , dtype='i')
        recvbuf = np.empty(num_of_data_per_rank, dtype='i')
        self.comms.scatter(input=input, recvbuf=recvbuf, dtype=self.comms.mpi.INT, root=0)
        if (rank == 0):
            print("Scattering Data : " + str(input) + ", from Rank " + str(rank) + "\n")


        print("Receiving Data : " + str(recvbuf) + ", from Rank " + str(rank) + "\n")


ex = ScatterExample()
ex.example()
