
import numpy as np
import shapely
import shapely.ops

from . import minkowski_funcs

class MFEuclideanCalculator:
    def __init__(self, quad_segs=8):
        self.quad_segs=quad_segs

    def calc_mfs(self, coords, r, quad_segs=None):
        """
        Create shapely Geometry object representing 
        the Minkowski sum of points and a disk with radius r.
        This dilation function is for Steiner-type formula for Euclidean distance.

        Parameters
        ----------
        coord     : array_like with shape (N_pt, 2)
        r         : float or array_like
            Specifies the circle radius in the Minkowski sum.
        quad_segs : int, default 8
            Specifies the number of linear segments in a quarter circle in 
            the approximation of circular arcs.

        Returns
        -------
        shapely.Polygon or shapely.MultiPolygon
            geometry object representing dilated points

        """
        if np.ndim(r) == 0:
            if r == 0:
                npt = coords.shape[0]
                return np.array([npt,0.,0.])
            else:
                geom = self.create_dilated_points_by_disk(coords, r, quad_segs)
                return minkowski_funcs.calc_mfs(geom)
        else:
            return np.stack(
                [
                    self.calc_mfs(coords, this_r, quad_segs)
                    for this_r in r
                ],
                axis=0
            )

    def calc_mfs_sequential(self, coords, arr_r, quad_segs=None):
        arr_dr = arr_r[1:] - arr_r[:-1]

        list_output = []

        r = arr_r[0]
        geom = self.create_dilated_points_by_disk(coords, r, quad_segs)
        list_output.append(minkowski_funcs.calc_mfs(geom))

        for dr in arr_dr:
            geom = geom.buffer(
                dr, 
                cap_style="round", 
                quad_segs=self.quad_segs if quad_segs is None else quad_segs
            )
            list_output.append(minkowski_funcs.calc_mfs(geom))
        
        return np.stack(
            list_output,
            axis=0
        )

    def create_dilated_points_by_disk(self, coords, r, quad_segs=None):
        """
        Create shapely Geometry object representing 
        the Minkowski sum of points and a disk with radius r
        This dilation function is for Steiner-type formula for Euclidean distance.

        Parameters
        ----------
        coord     : array_like with shape (N_pt, 2)
        r         : float
            Specifies the circle radius in the Minkowski sum.
        quad_segs : int, default 8
            Specifies the number of linear segments in a quarter circle in 
            the approximation of circular arcs.

        Returns
        -------
        shapely.Polygon or shapely.MultiPolygon
            geometry object representing dilated points

        """
        list_dilated_points  = [
            shapely.geometry.Point(*coord).buffer(r, cap_style='round', quad_segs=self.quad_segs if quad_segs is None else quad_segs)
            for coord in coords
        ]
        geom_dilated_points = shapely.ops.unary_union(list_dilated_points)
        return geom_dilated_points
