from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import itertools as it

locs = np.loadtxt('capitals.txt', dtype='str', delimiter=',')
labels = locs[:,0]
lats = locs[:,1]
lons = locs[:,2]
popus = locs[:,3]
# labels = str(labels)
for popu in popus:
    pops = int(popu)
    print(type(pops))

# # print (StringIO(str(labels)))

# # m = Basemap(llcrnrlon=100,llcrnrlat=80,urcrnrlon=4.,urcrnrlat=44.,
# #              resolution='l', projection='kav7', lat_0 = 39.5, lon_0 = -3.25)
m = Basemap(resolution='l', projection='kav7', lat_0 = 39.5, lon_0 = -3.25)
m.drawmapboundary()
m.drawcoastlines()
m.fillcontinents(color = 'coral', lake_color='aqua')
# m.drawparallels()
m.drawcountries()

def get_marker_color(population):
    # Returns green for small earthquakes, yellow for moderate
    #  earthquakes, and red for significant earthquakes.
    if population > 500000:
        return ('ro')
    elif population < 500000:
        return ('yo')
    else:
        return ('bo')


x, y = m(lons, lats)


for lb, xpt, ypt, pop in zip(labels, x, y, it.repeat(int(pops))):
    marker = get_marker_color(pop)
    m.plot(x, y, marker, markersize=5)
    # print(type(pop))
    plt.text(xpt, ypt, lb)
plt.title('Ini Peta')
plt.show()
