'''
17. [image] Render the Koch curve (fractal) in under 15 lines of code (module: turtle).
'''
from turtle import *
 
def koch_curve(length, order):
	if order == 0:
		forward(length)
	else:
		koch_curve(length/3, order-1)
		right(60)
		koch_curve(length/3, order-1)
		left(120)
		koch_curve(length/3, order-1)
		right(60)
		koch_curve(length/3, order-1)
	 
koch_curve(500, 4)
