import sys
sys.path.append('/home/vibhatha/github/bio/PythonMPI')
import pandas as pd
import numpy as np
from api import Constant
from sklearn.metrics.pairwise import euclidean_distances

class MDS2CSV:

    const = Constant.Constant()

    def get_mds_csv(self):
        damds_point_file = self.const.DAMDS_OUTPUT_POINTS_PATH
        damds_df = pd.read_csv(damds_point_file, usecols=[1, 2, 3], header=None, delim_whitespace=True)
        mds_dist_df = euclidean_distances(damds_df, damds_df)
        out_df = pd.DataFrame(mds_dist_df)
        out_df.to_csv(self.const.DAMDS_2_CSV_OUTPUT_PATH, header=False, index=False)


mds2csv = MDS2CSV()
mds2csv.get_mds_csv()
