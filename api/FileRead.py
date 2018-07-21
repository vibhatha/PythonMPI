import sys
from numpy import genfromtxt
import numpy as np

class FileRead:
    filepath = '/home/vibhatha/github/dsc-spidal-forks/applications/fungi-gene-sequence/data/distance_matrix.bin'

    def read(self, filepath):
        with open(filepath, mode='rb') as file:
            content = file.read()
            return content

    def lenth(self, filepath):
        with open(filepath) as file:
            for i,l in enumerate(file):
                pass
            return i+1

    def get_array_from_csv(self,filepath):
        arr = genfromtxt(filepath, delimiter=',', dtype=np.float64)
        return arr
