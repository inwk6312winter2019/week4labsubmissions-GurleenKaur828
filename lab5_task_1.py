import math
class Point:
	def __init__(self,x1,x2,y1,y2):
		self.x1=x1
		self.x2=x2
		self.y1=y1
		self.y2=y2
	def distance_between_points(self):
		dist = math.hypot(self.x2 - self.x1, self.y2 - self.y1)
		return dist
p=Point(12,15,18,20)
print(p.distance_between_points())
