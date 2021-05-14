#Distance Between Two Cities - Calculates the distance between two cities and allows the user to specify a unit of distance. This program may require finding coordinates for the cities like latitude and longitude.

import math

def distanceBetweenTwoCities(x1,y1,x2,y2):
	x1 = pow(x1 - x2, 2)
	y1 = pow(y1 - y2, 2)
	return math.sqrt(x1 + y1)
	
print(distanceBetweenTwoCities(2,2,5,5))

