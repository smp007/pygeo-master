


<!-- 

<script type="text/javascript" async
src="http://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js? 
config=TeX-MML-AM_CHTML"
</script>

This is commented out. -->



<img src="https://latex.codecogs.com/svg.image?$$f\left(I_{\max&space;},&space;t\right)=\left\{\begin{array}{cl}12&space;&&space;:&space;600<t<1000&space;\\\frac{I_{\max&space;}-12}{70}&space;t&plus;12&space;&:&space;1000<t<1070&space;\\I_{\max&space;}&space;&&space;:&space;1070<t<1160\end{array}\right.$$" 


PyGeo
=====

A Python package for three-dimensional geometry.


Installation
------------

Run
```
python -m pip install -e ".[dev]"
```
to install `pygeo` and all dependencies required for local development.


Testing
-------

Run
```
pytest tests
```
to run all the tests for `pygeo`.


Tasks
-----

1. Implement the missing `Ray` class. A [ray](https://en.wikipedia.org/wiki/Line_(geometry)#Ray) may be represented as its origin and a direction.

   1. Implement an `__init__` method that takes the origin and direction as argument and stores them as attributes on the instance.
   1. Implement a `__repr__` method.
   1. Implement an `__eq__` method that works by comparing both the origin and direction of the other ray. Provide tests for this method.

1. Implement the missing `Sphere` class. A [sphere](https://en.wikipedia.org/wiki/Sphere) may be represented by its center and a radius.

   1. Implement an `__init__` method that takes the center and radius as argument and stores them as attributes on the instance.
   1. Implement a `__repr__` method.
   1. Implement an `__eq__` method that works by comparing both the center and radius of the other sphere. Provide tests for this method.

1. Implement the missing `_intersect_ray_and_sphere` function. You may follow [this article](https://en.wikipedia.org/wiki/Line%E2%80%93sphere_intersection), but keep in mind that for a ray the parameter `d` mentioned in the article must be larger or equal to zero. Provide tests for this method.

As an optional extra exercise, implement

1. the missing `Triangle` class,
1. the missing `_intersect_ray_and_triangle` function and accompanying tests, and
1. the missing `intersect` that calls either `_intersect_ray_and_sphere` or `_intersect_ray_and_triangle` depending on the arguments.









.
