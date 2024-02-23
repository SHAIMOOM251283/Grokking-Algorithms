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

if __name__ == "__main__":
    while True:
        try:
            num_points = int(input("Enter the number of points to use for estimation (or 0 to exit): "))
            if num_points == 0:
                break
            estimated_pi = estimate_pi(num_points)
            print("Estimated value of pi:", estimated_pi)
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
