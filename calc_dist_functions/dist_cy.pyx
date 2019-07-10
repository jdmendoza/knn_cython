from libc.math cimport pow, sqrt, fabs
import numpy as np

def calc_dists_cy(double[:,:] dataset, double[:] input):

  cdef int N = dataset.shape[0]
  cdef int M = dataset.shape[1]
  cdef int i, j
  cdef double dist_temp
  cdef double[:] dists = np.zeros(N)

  for i in range(N):
    dist_temp = 0
    for j in range(M):
      dist_temp += pow(dataset[i][j] - input[j],2)
    dists[i] = sqrt(dist_temp)

  return np.asarray(dists)
