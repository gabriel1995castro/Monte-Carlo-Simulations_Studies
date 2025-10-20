#Libraries used:
import numpy as np
import matplotlib.pyplot as plt

#Project variables
num_simulations = 1000000
num_circle = 0

  
#randomizing a random value for x and y
x = np.random.uniform(-1, 1, num_simulations)
y = np.random.uniform(-1, 1, num_simulations)

#calculates the distance between the origin and the point
dist_points = x**2 + y**2
inside_circle = dist_points <= 1

for i in range(len(dist_points)):
    if dist_points[i]<1:
        num_circle += 1

#checking the values of pi contained in the circle
pi_est = 4 * num_circle/ num_simulations

#creating a visualization of the simulation for the user
sample_window = 4500
plt.figure(figsize=(5,5))

circle = plt.Circle((0, 0), 1, color='black', fill=False, linewidth=2)
plt.gca().add_patch(circle)
square = plt.Rectangle((-1, -1), 2, 2, fill=False, color='black', linewidth=2)
plt.gca().add_patch(square)

plt.scatter( x[:sample_window ][~inside_circle[:sample_window ]], y[:sample_window ][~inside_circle[:sample_window ]], color='red',
             s=1, label='Outside the circle')
plt.scatter( x[:sample_window ][inside_circle[:sample_window ]], y[:sample_window ][inside_circle[:sample_window ]], color='blue', 
            s=1, label='Inside the circle')
plt.gca().set_aspect('equal', adjustable='box')
plt.title(f'Estimated π = {pi_est:.6f}')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
