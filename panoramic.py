"""====================================================
                    DESCRIPTION

Functions for creating panoramic "front views" from a
point cloud.
=======================================================
"""
__author__ = 'Ronny Restrepo'

import numpy as np

def scale_to_255(a, min, max, dtype=np.uint8):
    return (((a - min) / float(max - min)) * 255).astype(dtype)

