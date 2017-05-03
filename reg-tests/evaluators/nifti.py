""" Evaluators for interfaces """

import numpy as np
import nibabel as nb

def get_img_size(filepath):
    """ Voxels that are not 0 """
    img = nb.load(filepath)
    return np.sum(img.get_data() > 0)
