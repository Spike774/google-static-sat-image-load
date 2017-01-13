# -*- coding: UTF-8 -*-

import numpy as np

# start_lat = 31942143
# start_lon = 120429449
# end_lat = 31961715
# end_lon = 120473276
# step = 13000

start_lat = 31.746920
start_lon = 120.097615
end_lat = 32.078480
end_lon = 120.785423
step = 0.013

# modi_lat = (int((end_lat - start_lat)/step) + 1)*step + start_lat
# modi_lon = (int((end_lon - start_lon)/step) + 1)*step + start_lon

# print len(range(start_lat, modi_lat, step)) * len(range(start_lon, modi_lon, step))
# print len(range(start_lat, end_lat, step)) * len(range(start_lon, end_lon, step))

# print float(start_lat)/ 1000000
a = np.arange(start_lat, end_lat, step)
b = np.arange(start_lon, end_lon, step)
# print len(range(start_lat, end_lat, step)) * len(range(start_lon, end_lon, step))
# for i in a:
#     print i
#     print len(a)
#
# for j in b:
#     print j
#     print len(b)
check_lat = 31.87692
check_lon = 120.734615

i_lat = 0
i_lon = 0
for lat in a:
    if lat >= check_lat:
        break
    i_lat += 1

for lon in b:
    if lon >= check_lon:
        break
    i_lon += 1

print 'index of lat is {0} / {1}\nindex of lon is {2} / {3}.'.format(i_lat, len(a), i_lon, len(b))
# usually use index_lat directly and use index_lon + 1
