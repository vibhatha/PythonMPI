import Communication
import numpy as np


class BcastRecvExample:
    comms = Communication.Communication()

    def example(self):
        rank = self.comms.comm.Get_rank()

        input = np.array([0, 1, 2, 3, 4], dtype='i')
        self.comms.bcast(input=input, dtype=self.comms.mpi.INT, root=0)
        if (rank == 0):
            print("Broadcasting Data : " + str(input) + ", from Rank " + str(rank) + "\n")


        print("Receiving Data : " + str(input) + ", from Rank " + str(rank) + "\n")


ex = BcastRecvExample()
ex.example()
