import math
import collections
 
Point2D = collections.namedtuple('Point2D', ['x', 'y'])
 
p1 = Point2D(x=30, y=20)
p2 = Point2D(x=60, y=50)
 
a = p1.x - p2.x
b = p1.y - p2.y
 
c = math.sqrt((a * a) + (b * b))
print(c)