# Voronoi diagram generator

This program was created to visualize what a Voronoi diagram looks like, using Pillow package in Python.

# Installation and usage

To use the program, you need to install a single dependency: `pip install pillow`.

The VoronoiGenerator class creates a 512x512 (default resolution, it can be messed with) NumPy Array and generates a colorful [Voronoi diagram](https://en.wikipedia.org/wiki/Voronoi_diagram), which is a special kind of partition of a plane. First, it creates a specific number (the `no_points` property) of randomly scattered points with associated colors and then changes every pixel to the color of the closest point. Then, points are represented by the black 3x3 dots. Program displays the diagram visually using Pillow package.

The program can be modified, for example by changing the type of distance to Manhattan metric, giving more interesting results. Algorithm used to generate this diagram is very naive, but I plan to modify it in the future using more advanced algorithms or by writing it using C# and Compute Shaders.
