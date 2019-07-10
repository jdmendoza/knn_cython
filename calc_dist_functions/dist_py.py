import math

def calc_dists_py(data, input):
    dist = []
    row_len = len(data[0])
    col_len = len(data)

    for i in range(col_len):
        dist_temp = 0
        for j in range(row_len):
            dist_temp += (data[i][j] - input[j])**2
        dist.append(math.sqrt(dist_temp))
    return dist
