# -*- coding: UTF-8 -*-

import numpy as np

start_lat = 31.746920
start_lon = 120.097615
end_lat = 32.078480
end_lon = 120.785423
step = 0.013

a = np.array([[0, 0]], dtype=float)

for lat in np.arange(start_lat, end_lat, step):
    for lon in np.arange(start_lon, end_lon, step):
        b = np.array([[lat, lon]], dtype=float)
        # print b
        a = np.concatenate((a, b))
i = 0

lat_list = np.arange(start_lat, end_lat, step)
lon_list = np.arange(start_lon, end_lon, step)

# break at 33th image

total_num = len(lat_list) * len(lon_list)

# for v in a:
#     i += 1
#     print v
#     print v[0]
#     print v[1]

print a[106][0], a[106][1]

# print i, total_num
