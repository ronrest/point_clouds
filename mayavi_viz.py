"""====================================================
                    DESCRIPTION
Visualisations of point cloud data using the mayavi
library
=======================================================
"""
__author__ = 'Ronny Restrepo'

import numpy as np
import mayavi.mlab


# ==============================================================================
#                                                                     VIZ_MAYAVI
# ==============================================================================
def viz_mayavi(points, vals="distance"):
    """ Interactively visualize the point cloud data using mayavi
    
    Args:
        points: (numpy array)
            array of shape at least nx3 containing the point cloud data
            n rows representing each point.
            3 or more values for each point, with the first three
            representing the x,y,z coordinates
        vals: (str) (default="distance")
            What values to use for color coding.
            "distance" = the calculated distance of each point from the origin
                         when looked at from the top
            "height" = the z values of the point cloud data
    """
    x = points[:, 0]  # x position of point
    y = points[:, 1]  # y position of point
    z = points[:, 2]  # z position of point
    # r = points[:, 3]  # reflectance value of point
    d = np.sqrt(x ** 2 + y ** 2)  # Map Distance from sensor

    if vals == "height":
        col = z
    else:
        col = d

    fig = mayavi.mlab.figure(bgcolor=(0, 0, 0), size=(640, 360))
    mayavi.mlab.points3d(x, y, z,
                         col,          # Values used for Color
                         mode="point",
                         colormap='spectral', # 'bone', 'copper', 'gnuplot'
                         # color=(0, 1, 0),   # Used a fixed (r,g,b) instead
                         figure=fig,
                         )
    mayavi.mlab.show()
    
    
