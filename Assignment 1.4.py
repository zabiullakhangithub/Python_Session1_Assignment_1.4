# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 11:06:49 2018

@author: zabiulla.khan

Write a Python program to find the volume of a sphere with diameter 12 cm.
Formula: V=4/3 * π * r3
"""
# Value of π(pi)
pi = 3.14159

#value of radius/diameter , radius = 1/2 diameter
diameter = 12
radius = (1/2)*diameter

# Implement the formula 
radius_cube = radius*radius*radius

V=(4/3)*pi*(radius_cube)
print("Volume of a sphere with 12cm: ", V)