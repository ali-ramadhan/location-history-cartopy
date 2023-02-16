import os
import json

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mimage
import cartopy.crs as ccrs
import cartopy.feature as cfeature

from PIL import Image
Image.MAX_IMAGE_PIXELS = 1000000000

with open("Records.json", "r") as f:
    location_history = json.load(f)
    locations = location_history["locations"]
    n_locations = len(locations)

    lats = np.zeros(n_locations)
    lons = np.zeros(n_locations)

    for i, location in enumerate(locations):
        lats[i] = location["latitudeE7"] / 1e7
        lons[i] = location["longitudeE7"] / 1e7


fig = plt.figure(figsize=(32, 18))
ax = plt.axes(projection=ccrs.PlateCarree())

extent = [232, 300.5, 23, 50]
ax.set_extent(extent, crs=ccrs.PlateCarree())

# Use a much higher resolution map image, e.g. https://www.naturalearthdata.com/downloads/10m-raster-data/10m-cross-blend-hypso/
fname = os.path.join("HYP_HR_SR_OB_DR", "HYP_HR_SR_OB_DR.tif")
ax.imshow(mimage.imread(fname), origin="upper", transform=ccrs.PlateCarree(), extent=[-180, 180, -90, 90])

# ax.add_feature(cfeature.COASTLINE.with_scale("10m"), linewidth=0.5, alpha=1, facecolor="None", edgecolor="black")
ax.add_feature(cfeature.BORDERS.with_scale("10m"), linewidth=0.5, alpha=1, facecolor="None", edgecolor="black")
ax.add_feature(cfeature.STATES.with_scale("10m"), linewidth=0.5, alpha=1, facecolor="None", edgecolor="black")

ax.scatter(lons, lats, marker=".", s=0.5, color="red", alpha=0.5)

ax.axis("off")
fig.set_tight_layout(True)

plt.savefig("location_history.png", bbox_inches="tight", pad_inches=0)
