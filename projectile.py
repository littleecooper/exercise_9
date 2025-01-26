# This is to import the modules pi, tan and cos to use in the code - all other math functions are not required
from math import pi, tan, cos
# If I had imported just math then I would be able to use all the functions but I would have to write it as math.tan()

# height of the barrel
y0 = 1
# the horizontal distance travelled
x = 0.5
# elevation degree
deg = 80
# the initial velocity m/s
v0 = 44
# acceleration due to gravity
g = 9.81
# All of these values have been taken from the exercise guide on mimeo

# theta = elevation angle in radians (from exercise guide)
# pi has been imported from the math module at the top thus, we do not need to specify it
theta = deg * (pi/180)
# we wanted to print this to ensure the theta equation was working properly
print(theta)

# tan and cos have been imported from the math function
projectile_height = y0 + (x * tan(theta)) - ((g * x**2) / (2 * (v0 * cos(theta)) **2))
# If you click on command (Mac) and hover over tan and cos, it tells you they are functions and this is why they require brackets after the word
# The print function is so we can see what the answer to the value is.
# the * multiplies the value
# the ** squares the value
# theta is in the tan and cos because it is asking for a value measured in radians which is what theta is measured in
print(projectile_height)