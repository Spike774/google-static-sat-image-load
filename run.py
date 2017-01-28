# -*- coding: UTF-8 -*-

import numpy as np
import csv
import urllib
import time
import random
import os

# start_lat = 31.746920
# start_lon = 120.097615
# end_lat = 32.078480
# end_lon = 120.785423
# step = 0.013

start_lat = 33.749859
start_lon = 120.143627
end_lat = 33.823136
end_lon = 120.350032
step = 0.013

# GOGL_WEB_KEY = os.environ.get('GOGL_WEB_KEY')
GOGL_WEB_KEY = 'AIzaSyB_vS8wf9C2OlYitOuogXYFR0yr2eZ1czg'

# coords cache 32.078480 120.097615, 31.746920 120.785423
# start_lat = 31.942143
# start_lon = 120.429449
# end_lat = 31.961715
# end_lon = 120.473276


lat_list = np.arange(start_lat, end_lat, step)
lon_list = np.arange(start_lon, end_lon, step)

# break at 33th image

total_num = len(lat_list) * len(lon_list)

# csv_file = file('scan_coords.csv', 'wb')
# writer = csv.writer(csv_file, delimiter=';')

a = np.array([[0, 0]], dtype=float)

for lat in np.arange(start_lat, end_lat, step):
    for lon in np.arange(start_lon, end_lon, step):
        b = np.array([[lat, lon]], dtype=float)
        # print b
        a = np.concatenate((a, b))

flag = 2

i = flag

for v in a[flag:]:
    lat = v[0]
    lon = v[1]

    urlparams = urllib.urlencode({'center': '{0},{1}'.format(lat, lon),
                                  'zoom': 16,
                                  'size': '600x625',
                                  'maptype': 'satellite',
                                  'key': GOGL_WEB_KEY})
    url = 'https://maps.googleapis.com/maps/api/staticmap?' + urlparams

    print 'now saving... {0}/{1} ...'.format(i, total_num)

    urllib.urlretrieve(url, "image_cache/sate_c_{0}_{1}_z_16.png".format(lat, lon))

    with open('scan_coords.csv', 'ab') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow([i, "image_cache/sate_c_{0}_{1}_z_16.png".format(lat, lon), lat, lon])

    i += 1

    t = random.randint(1, 3)
    time.sleep(t)

# csv_file.close()
print '*** mission complete ***'
