from api import Communication

class SendRecvExample:
    comms = Communication.Communication()

    def example(self):
        rank = self.comms.comm.Get_rank()

        if (rank == 0):
            input = [0,1,2,3,4]
            self.comms.isend(input=input, dest=1, tag=11)
            print("Sending Data : " + str(input) + "from Rank " + str(rank))

        elif (rank == 1):
            data = self.comms.irecv(source=0, tag=11)
            print("Receiving Data : " + str(data) + "from Rank " + str(rank))


ex = SendRecvExample.example()
