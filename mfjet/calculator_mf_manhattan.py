
import math

import numpy as np
import shapely
import shapely.ops

from . import minkowski_funcs

class MFManhattanCalculator:
    def __init__(self):
        pass

    def calc_mfs(self, coords, r):
        if np.ndim(r) == 0:
            if r == 0:
                npt = coords.shape[0]
                return np.array([npt,0.,0.])
            else:
                geom = self.create_dilated_points_by_square(coords, r)
                return minkowski_funcs.calc_mfs(geom)
        else:
            return np.stack(
                [
                    self.calc_mfs(coords, this_r)
                    for this_r in r
                ],
                axis=0
            )

    def calc_mfs_sequential(self, coords, arr_r):
        arr_dr = arr_r[1:] - arr_r[:-1]

        list_output = []

        geom = self.create_dilated_points_by_square(coords, arr_r[0])
        list_output.append(minkowski_funcs.calc_mfs(geom))

        for dr in arr_dr:
            geom = geom.buffer(dr, cap_style="square", join_style="mitre", mitre_limit=math.inf)
            list_output.append(minkowski_funcs.calc_mfs(geom))
        
        return np.stack(
            list_output,
            axis=0
        )

    def create_dilated_points_by_square(self, coords, r):
        """
        Create shapely Geometry object representing the Minkowski sum of points and a disk with radius r
        This dilation function is for Steiner-type formula for Euclidean distance.

        Parameters
        ----------
        coord     : array_like with shape (N_pt, 2)
        r         : float
            Specifies the circle radius in the Minkowski sum.
        quad_segs : int, default 8
            Specifies the number of linear segments in a quarter circle in the approximation of circular arcs.

        Returns
        -------
        shapely.Polygon or shapely.MultiPolygon
            geometry object representing dilated points

        """
        list_dilated_points  = [
            shapely.geometry.Point(*coord).buffer(r, cap_style='square', join_style="mitre", mitre_limit=math.inf)
            for coord in coords
        ]
        geom_dilated_points = shapely.ops.unary_union(list_dilated_points)
        return geom_dilated_points
