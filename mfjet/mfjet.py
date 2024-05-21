import numpy as np

import shapely
from shapely import geometry, ops


def calc_mfs_from_coords(coords, r):
    #list_points = [shapely.geometry.Point(*coord) for coord in coords]
    #shape_points  = shapely.ops.unary_union(list_points)
    #shape_dilated = shape_points.buffer(r, cap_style=1)
    
    list_circles  = [shapely.geometry.Point(*coord).buffer(r, cap_style=1) for coord in coords]
    shape_dilated = shapely.ops.unary_union(list_circles)

    return calc_mfs(shape_dilated)


def calc_mf_seq_from_coords(coords, arr_r):
    r0 = arr_r[0]
    arr_delta_r = arr_r[1:] - arr_r[:-1]

    list_mf_seq = []

    list_circles = [shapely.geometry.Point(*coord).buffer(r0, cap_style=1) for coord in coords]
    shape_dilated  = shapely.ops.unary_union(list_circles)
    list_mf_seq.append(calc_mfs(shape_dilated))

    for delta_r in arr_delta_r:
        shape_dilated = shape_dilated.buffer(delta_r, cap_style=1)
        list_mf_seq.append(calc_mfs(shape_dilated))
    return np.stack(list_mf_seq,axis=0)


def calc_mfs(shape):
    return np.array([
        calc_area(shape),
        calc_length(shape),
        calc_euler(shape)
    ])

def calc_area(shape):
    return shape.area
def calc_length(shape):
    return shape.boundary.length
def calc_euler(shape):
    if type(shape) is shapely.geometry.MultiPolygon:
        #print("MultiPolygon")
        euler = sum([calc_euler_poly(geom) for geom in shape.geoms])
    elif type(shape) is shapely.geometry.Polygon:
        #print("Polygon")
        euler = calc_euler_poly(shape)
    else:
        assert False, "unsupported type: {}".format(type(shape))
    return euler
def calc_euler_poly(poly):
    num_exteriors = 1
    num_interiors = len(poly.interiors)
    return num_exteriors - num_interiors
