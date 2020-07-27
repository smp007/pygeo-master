from pygeo.intersect import (
    intersect,
    _intersect_ray_with_sphere,
    _intersect_ray_with_triangle,
)
from pygeo.objects import Ray, Sphere, Triangle, Point, Vector
import numpy as np

# intersect


# _intersect_ray_with_sphere
def test__intersect_ray_with_sphere__does_not_intersect():
    R = Ray(Point((0,0,4)),Vector((1,0,0)))
    S = Sphere(Point((0,0,0)),3)
    assert (_intersect_ray_with_sphere(R,S)=="Does not intersect") is True

def test__intersect_ray_with_sphere__one_point_intersection():
    R = Ray(Point((0,0,3)),Vector((1,0,0)))
    S = Sphere(Point((0,0,0)),3)
    assert (_intersect_ray_with_sphere(R,S)==Point((0,0,3))) is True

def test__intersect_ray_with_sphere__two_point_intersection():
    R = Ray(Point((0,0,2)),Vector((1,0,0)))
    S = Sphere(Point((0,0,0)),3)
    val = np.sqrt(5)
    assert (_intersect_ray_with_sphere(R,S) == (Point((val,0,2)),Point((-val,0,2)))) is True




# _intersect_ray_with_triangle
