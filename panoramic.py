"""====================================================
                    DESCRIPTION

Functions for creating panoramic "front views" from a
point cloud.
=======================================================
"""
__author__ = 'Ronny Restrepo'

import numpy as np

# ==============================================================================
#                                                                   SCALE_TO_255
# ==============================================================================
def scale_to_255(a, min, max, dtype=np.uint8):
    """ Scales an array of values from specified min, max range to 0-255
        Optionally specify the data type of the output (default is uint8)
    """
    return (((a - min) / float(max - min)) * 255).astype(dtype)

