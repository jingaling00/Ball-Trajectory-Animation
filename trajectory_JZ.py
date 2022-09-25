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

# User inputs
radius = 15 # int(input('Enter Radius (a number between 10 and 20 inclusive): '))
initial_speed = 80 #input('Enter initial speed (a number between 30 and 80 inclusive): ')
initial_angle = 90 #input('Enter a number for initial trajectory angle in degrees (30-90 inclusive)": ')
initial_angle = initial_angle * math.pi / 180
time_incr = 0.3 #input('Enter a value for the simulation time increment: ')
    
height = ((initial_speed**2)/(2*G)) * ((math.sin(initial_angle))**2) # height of ball
max_height = math.floor(height + (3*radius)) # window height
window_range = ((initial_speed**2)/G) * (math.sin(2*initial_angle)) # horizontal displacement of ball
max_range = math.floor(2 * (window_range + (3*radius))) # window size x-axis

# Create graphics window
win = GraphWin('Trajectory',max_range,max_height)
center_point = Point(15,max_height-15)

# Define Circle
circle = Circle(central_point, radius)
# Set colors
circle.setFill('yellow')
# Draw circle
circle.draw(win)

time_of_flight = (2*initial_speed/G) * math.sin(initial_angle)
num_steps = math.ceil(time_of_flight / time_incr)

dx = (initial_speed * math.cos(initial_angle)) * time_incr

t = 0

while (circle.getCenter().getX() + radius < (max_range)):
    dy = ((initial_speed * math.sin(initial_angle)) - (G*(t))) * time_incr
    dx = (initial_speed * math.cos(initial_angle)) * time_incr
    circle.move(dx,-dy)  
    t += time_incr
    time.sleep(time_incr)
    if (circle.getCenter().getY() + radius) >= (max_height):
        initial_speed*=0.54
        t = 0
        continue


""" DO NOT MODIFY OR WRITE ANYTHING BELOW """

# Close after mouse click
try:
    win.getMouse()    
    win.close()
except:
    pass