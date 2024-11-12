"""
NOT streamlit, but there is an mpld3 component for streamlit... 


modified from mpld3 imshow example with mouse position, 

run it then open the saved html file 

"""
import matplotlib.pyplot as plt
import numpy as np
import yt


import mpld3
from mpld3 import plugins

ds = yt.load("IsolatedGalaxy/galaxy0030/galaxy0030")
field = ('gas', 'density')
axis = 'z'
slc = yt.SlicePlot(ds, axis, field, buff_size=(2000,2000))
slc.render()
fig = slc.plots[field].figure

plugins.connect(fig, plugins.MousePosition(fontsize=14))

mpld3.save_html(fig, 'iso_gal_z_axis.html')
