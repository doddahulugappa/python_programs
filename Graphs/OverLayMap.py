import cartopy.crs as ccrs
import cartopy.io.img_tiles as cimgt
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

import windrose

ws = np.random.random(500) * 6
wd = np.random.random(500) * 360

minlon, maxlon, minlat, maxlat = (6.5, 7.0, 45.85, 46.05)

proj = ccrs.PlateCarree()
fig = plt.figure(figsize=(12, 6))
# Draw main ax on top of which we will add windroses
main_ax = fig.add_subplot(1, 1, 1, projection=proj)
main_ax.set_extent([minlon, maxlon, minlat, maxlat], crs=proj)
main_ax.gridlines(draw_labels=True)
main_ax.coastlines()

request = cimgt.OSM()
main_ax.add_image(request, 12)

# Coordinates of the station we were measuring windspeed
cham_lon, cham_lat = (6.8599, 45.9259)
passy_lon, passy_lat = (6.7, 45.9159)

# Inset axe it with a fixed size
wrax_cham = inset_axes(
    main_ax,
    width=1,  # size in inches
    height=1,  # size in inches
    loc="center",  # center bbox at given position
    bbox_to_anchor=(cham_lon, cham_lat),  # position of the axe
    bbox_transform=main_ax.transData,  # use data coordinate (not axe coordinate)
    axes_class=windrose.WindroseAxes,  # specify the class of the axe
)

# Inset axe with size relative to main axe
height_deg = 0.1
wrax_passy = inset_axes(
    main_ax,
    width="100%",  # size in % of bbox
    height="100%",  # size in % of bbox
    # loc="center",  # don"t know why, but this doesn"t work.
    # specify the center lon and lat of the plot, and size in degree
    bbox_to_anchor=(
        passy_lon - height_deg / 2,
        passy_lat - height_deg / 2,
        height_deg,
        height_deg,
    ),
    bbox_transform=main_ax.transData,
    axes_class=windrose.WindroseAxes,
)

wrax_cham.bar(wd, ws)
wrax_passy.bar(wd, ws)
for ax in [wrax_cham, wrax_passy]:
    ax.tick_params(labelleft=False, labelbottom=False)
    plt.show()