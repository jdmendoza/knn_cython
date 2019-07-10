import pandas as pd
import numpy as np
from collections import Counter

from calc_dist_functions.dist_py import calc_dists_py
from calc_dist_functions.dist_cy import calc_dists_cy

class kNearestNeighbors():
    def __init__(self, data, targets, dist_func, neighbors):
        self._data = data
        self._targets = targets
        self._dist_func = dist_func
        self._neighbors = neighbors

    def raw_distances(self, input):
        return self._dist_func(self._data, input)

    def predict(self, input):
        distances = self._dist_func(self._data, input)
        neighbors = sorted(zip(distances, self._targets), key=lambda x: x[0])[0:self._neighbors]

        return Counter([n[1] for n in neighbors]).most_common(1)[0][0]

if __name__ == "__main__":
    df = pd.read_csv("data/data_banknote_authentication.txt", names=['f1','f2','f3','f4','target'])
    target = df.pop('target')

    knn_py = kNearestNeighbors(df.values, target, calc_dists_py, 5)
    print (knn_py.find_neighbors(df.values[-1]))

    knn_cy = kNearestNeighbors(df.values, target, calc_dists_cy, 5)
    print (knn_cy.find_neighbors(df.values[-1]))
