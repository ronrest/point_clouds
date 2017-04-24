"""====================================================
                    DESCRIPTION

Functions for top views of point cloud data
=======================================================
"""
__author__ = 'ronny'



import numpy as np
def scale_to_255(a, min, max, dtype=np.uint8):
    return (((a - min) / float(max - min)) * 255).astype(dtype)

