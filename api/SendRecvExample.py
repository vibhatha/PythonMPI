import Communication
import numpy as np

class SendRecvExample:
    comms = Communication.Communication()

    def example(self):
        rank = self.comms.comm.Get_rank()

        if (rank == 0):
            input = np.array([0,1,2,3,4])
            self.comms.send(input=[input, self.comms.mpi.INT], dest=1, tag=11)
            print("Sending Data : " + str(input) + ", from Rank " + str(rank) + "\n")

        elif (rank == 1):
            data = self.comms.recv(source=0, tag=11)
            print(type(data))
            print("Receiving Data : " + str(data) + ", from Rank " + str(rank) + "\n")


ex = SendRecvExample()
ex.example()
