# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 19:54:11 2022

@author: jingy
"""

# -*- coding: utf-8 -*-
"""
Template code


1) Get the user inputs
2) Generate a window with the appropriate size based on the user inputs
3) Place the initial circle (ball) in the window as described in the instruction
4) Run the simulation and check when the ball hits the horizontal edge. Make the necessary adjustment
5) Termiunate the simulation when the stopping criteria is reached.



"""
from graphics import *
import time
import math

""" Write your code here """

G = 9.8 # gravity

def trajectory(v0, theta, radius, time_incr):
    # Convert degrees to radians
    theta = theta * math.pi / 180
    
    # Set window size
    y_traj = ((v0**2)/(2*G)) * ((math.sin(theta))**2) # height of ball
    max_y = math.floor(y_traj + (3*radius)) # window height
    x_traj = ((v0**2)/G) * (math.sin(2*theta)) # horizontal displacement of ball
    max_x = math.floor(2 * (x_traj + (3*radius))) # window size x-axis
    
    # Create graphics window
    win = GraphWin('Trajectory',max_x,max_y)
    center_point = Point(15,max_y-15)
    # Define Circle
    circle = Circle(center_point, radius)
    # Set colors
    circle.setFill('yellow')
    # Draw circle
    circle.draw(win)

    time_of_flight = (2*v0/G) * math.sin(theta)
    num_steps = math.ceil(time_of_flight / time_incr)
    
    t = 0 # initial time
    T = 0.04 # pause in seconds between every move
    iteration_counter = 0
    while (circle.getCenter().getX() + radius) < max_x:
        dy = ((v0 * math.sin(theta)) - (G*(t))) * time_incr
        dx = (v0 * math.cos(theta)) * time_incr
        if (circle.getCenter().getY() + radius) > (max_y-1) and t > 0: # Check if ball has crossed x-axis
            v0*=0.56
            t = 0
            continue
        elif math.isclose(dy,0,abs_tol=0.0001): # Stop ball from bouncing
            break
        else:
            circle.move(dx,-dy)
        t += time_incr
        time.sleep(T)
        if iteration_counter > 0: 
            print(f'iteration {iteration_counter} , dx = {dx:.3f}, dy = {dy:.3f}')
        iteration_counter+=1
    print('done')
        
if __name__ == '__main__':
    # User input for radius
    radius = int(input('Enter Radius (a number between 10 and 20 inclusive): '))
    while radius > 20 or radius < 10:
        print('\nError. Please enter radius between 10 and 20, inclusive.')
        radius = int(input('Enter Radius (a number between 10 and 20 inclusive): '))
        
    # User input for initial speed
    v0 = int(input('Enter initial speed (a number between 30 and 80 inclusive): '))
    while v0 > 80 or v0 < 30:
        print(f'\nError. Please enter initial speed between 30 and 80, inclusive.')
        v0 = int(input('Enter initial speed (a number between 30 and 80 inclusive): '))
    
    # User input for initial angle
    theta = int(input('Enter initial trajectory angle in degrees (30-90 inclusive): '))
    while theta > 90 or theta < 30:
        print(f'\nError. Please enter initial angle between 30 and 90 degrees, inclusive.')
        theta = int(input('Enter initial trajectory angle in degrees (30-90 inclusive)": '))
    
    # User input for time increment
    time_incr = float(input('Enter a value for the simulation time increment: '))
    
    # Run trajectory of ball
    trajectory(v0,theta,radius,time_incr)

""" DO NOT MODIFY OR WRITE ANYTHING BELOW """

# Close after mouse click
try:
    win.getMouse()    
    win.close()
except:
    pass
