#!/usr/bin/python
# Filename : square1.py

from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()

def square(t):
	for i in range(4):
		fd(t, 100)
		lt(t)

p = square(bob)

wait_for_user()
