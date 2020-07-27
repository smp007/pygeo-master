from pygeo.objects import Ray, Sphere, Triangle, Point, Vector
import numpy as np


def intersect(first_object, second_object):
    ...


def _intersect_ray_with_sphere(ray, sphere):  
    """Function which provides the co-ordinates of intersection."""
    o = ray._origin
    u = ray._direction
    r = sphere._radius
    c = sphere._center
    norm_u = np.linalg.norm(u._vector)
    U = (1/norm_u) * u._vector              #finds the unit direction

    b = 2 * np.dot(u._vector,(o-c)._vector)
    a = 1
    c = np.dot((o-c)._vector,(o-c)._vector) - r**2
    discriminant = b**2 - 4*a*c             
    

    if discriminant > 0:
        """two point intersection case."""
        square_root_discriminant = np.sqrt(discriminant)
        d1 = (-1*b + square_root_discriminant)/ (2*a)
        d2 = (-1*b - square_root_discriminant)/ (2*a)        
        p1 = Point(o._point + (d1 * U))
        p2 = Point(o._point + (d2 * U))
        return p1,p2
        
    elif discriminant == 0:
        """one point interscetion case."""
        d = -1*b / 2*a
        p = Point(o._point +(d*U))
        return p

    else:
        return "Does not intersect"



def _intersect_ray_with_triangle(ray, triangle):
    ...

