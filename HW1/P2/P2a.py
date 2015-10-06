from P2 import *
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

import findspark
findspark.init()

import pyspark
sc = pyspark.SparkContext(appName="P2")


rdd1 = np.arange(2000)
rdd2 = np.arange(2000)

rdd1 = sc.parallelize(rdd1, 10)
rdd2 = sc.parallelize(rdd2, 10)

pixels = rdd1.cartesian(rdd2)
res = pixels.map(lambda a: (a,mandelbrot((a[1]/500.0) - 2,(a[0]/500.0) - 2)))
draw_image(res)
a = sum_values_for_partitions(res)
to_plot = a.collect()

plt.hist(to_plot)
plt.title('Load distribution with default partitioning')
plt.ylabel('Count')
plt.xlabel('Load')
plt.show()
