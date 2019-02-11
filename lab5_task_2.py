import math
class Point:
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def distance_between_points(p1,p2):
                dist = math.hypot(p2.x - p1.x, p2.y - p1.y)
                return dist
p=Point(10,12)
q=Point(20,30)
print(p.distance_between_points(q))

class Rectangle:
	def __init__(self,width=200,height=100,corner=Point()):
		self.width=width
		self.height=height
		self.corner=corner.Point()
box=Rectangle()

def find_center(shape):
	cx=box.corner.p.distance_between_points(q)+(box.width)/2
	cy=box.corner.p.distance_between_points(q)+(box.height)/2
	print(x,y)
find_center(box)

