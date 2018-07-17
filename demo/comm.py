import mpi4py
mpi4py.rc.recv_mprobe = False
from mpi4py import  MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()


print(rank)

