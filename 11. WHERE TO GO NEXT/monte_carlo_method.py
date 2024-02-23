import random

def estimate_pi(num_points):
    points_inside_circle = 0
    total_points = num_points
    
    for _ in range(num_points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        
        # Check if the point is inside the unit circle
        if x**2 + y**2 <= 1:
            points_inside_circle += 1
    
    # The ratio of points inside the circle to total points is approximately equal to pi/4
    return 4 * points_inside_circle / total_points

# Number of random points to generate
num_points = 100000

# Estimate the value of pi using the Monte Carlo method
estimated_pi = estimate_pi(num_points)
print("Estimated value of pi:", estimated_pi)

# One simple example of a probabilistic algorithm is the Monte Carlo method for estimating the value of π (pi) by randomly sampling points 
# in a square and determining how many fall within a quarter of a unit circle.