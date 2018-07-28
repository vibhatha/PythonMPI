parallelheatmap:
	mpirun -n 4 python distributed/ParallelHeatMapGen.py 100

tasks:
	mpirun -n 4 python distributed/ParallelHeatMapGen.py 10;mpirun -n 4 python distributed/ParallelHeatMapGen.py 15;mpirun -n 4 python distributed/ParallelHeatMapGen.py 15;mpirun -n 4 python distributed/ParallelHeatMapGen.py 50;mpirun -n 4 python distributed/ParallelHeatMapGen.py 100
