#!/home/vibhatha/venv/ENV3/bin/python3
import numpy as np
import mpi4py

mpi4py.rc(initialize=False, finalize=False)
from mpi4py import MPI

MPI.Init()

comm = MPI.COMM_WORLD
world_rank = comm.Get_rank()
world_size = comm.Get_size()

# use ./worker bash script for simpler representation
# Spawn call returns a InterComm object
children = comm.Spawn("runner", maxprocs=2, root=0)

parent = comm.Get_parent()

data = np.array([1, 2, 3, 4], dtype='i')
# comm.Bcast([data, MPI.INT], root=0)
if world_rank == 0:
    children.Send([data, MPI.INT], dest=1, tag=0)
print("From Master: ", world_rank, world_size, parent)

# comm.free()

MPI.Finalize()
