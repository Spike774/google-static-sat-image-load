# -*- coding: UTF-8 -*-

import numpy as np
import csv


start_lat = 31.746920
start_lon = 120.097615
end_lat = 32.078480
end_lon = 120.785423
step = 0.013

lat_list = np.arange(start_lat, end_lat, step)
lon_list = np.arange(start_lon, end_lon, step)

a = np.array([[0, 0]], dtype=float)

for lat in np.arange(start_lat, end_lat, step):
    for lon in np.arange(start_lon, end_lon, step):
        b = np.array([[lat, lon]], dtype=float)
        a = np.concatenate((a, b))



for v in a[1:]:
    lat = v[0]
    lon = v[1]
    with open('image_name_list.csv', 'ab') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(["image_cache\sate_c_{0}_{1}.png".format(lat, lon)])

print '*** mission complete ***'
