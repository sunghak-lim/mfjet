"""
Collection of dilation functions.

"""

import shapely
import shapely.ops

def create_dilated_points_by_disk(coords, r, quad_segs=8):
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
        shapely.geometry.Point(*coord).buffer(r, cap_style='round', quad_segs=quad_segs)
        for coord in coords
    ]
    geom_dilated_points = shapely.ops.unary_union(list_dilated_points)
    return geom_dilated_points


def create_dilated_points_by_square(coords, r):
    """
    Create shapely Geometry object representing the Minkowski sum of points and a square with half-width r
    This dilation function is for Steiner-type formula for Manhattan distance.

    Parameters
    ----------
    coord  : array_like with shape (N_pt, 2)
    r      : float
        Specifies the circle radius in the Minkowski sum.

    Returns
    -------
    shapely.Polygon or shapely.MultiPolygon
        geometry object representing dilated points

    """
    list_dilated_points  = [
        shapely.geometry.Point(*coord).buffer(r, cap_style='square')
        for coord in coords
    ]
    geom_dilated_points = shapely.ops.unary_union(list_dilated_points)
    return geom_dilated_points
