import numpy as np


"""
In this file, we perform the computation of the minimizers.
To minimize the sum of squared distance, we can just compute the mean (Centroid) of the 2D coordinates
To minimize the sum of distances, we have to use numerical method. We look for the so called "Geometric median"
if the points. No closed form solution exists to such a problem
"""

def compute_centroid(points):

    N = len(points)

    x_c = 0
    y_c = 0

    for point in points:
        x_c += point[0]
        y_c += point[1]

    x_c = x_c / N
    y_c = y_c / N

    return [x_c, y_c]


"""
Here we compute the gradient of the sum of distances with respect to our current geometric median.
This takes O(N) time
"""
def compute_gradient(geom_x, geom_y, points):

    gradient_x = 0
    gradient_y = 0

    for i in range(len(points)):

        x_coord = points[i][0]
        y_coord = points[i][1]

        if x_coord != geom_x:
            gradient_x += -(x_coord - geom_x)/(np.sqrt((x_coord - geom_x)**2 + (y_coord - geom_y)**2 ))

        if y_coord != geom_y:
            gradient_y += -(y_coord - geom_y)/(np.sqrt((x_coord - geom_x)**2 + (y_coord - geom_y)**2 ))

    return [gradient_x,gradient_y]


def compute_geometric_median(points, alpha, max_iter,epsilon):

    """
    We use gradient descent as a numerical method to find the geometric median
    """

    """
    The centroid is a good initialization for gradient descent
    """
    geom_x , geom_y = compute_centroid(points)


    """
    Gradient descent here
    """
    for _ in range(max_iter):

        prev_x, prev_y = geom_x, geom_y

        gradient_x, gradient_y = compute_gradient(geom_x, geom_y, points)

        geom_x -= alpha * gradient_x
        geom_y -= alpha * gradient_y


        """
        Stop at convergence
        """
        if (geom_x-prev_x)**2 + (geom_y-prev_y)**2 < epsilon:
            break

    return [geom_x,geom_y]
