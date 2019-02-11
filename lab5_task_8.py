class Point(object):
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
	def __add__(self, other):
		point = Point()
		if isinstance(other, Point):
			point.x += self.x + other.x
			point.y += self.y + other.y
			return point
		elif type(other) == tuple:
			point.x += self.x + other[0]
			point.y += self.y + other[1]
			return point
	def __radd__(self, other):
		return self.__add__(other)
	def __str__(self):
		return "(%s, %s)" % (self.x, self.y)
point1 = Point(2, 7)
point2 = Point(9, 3)
point3 = point1 + point2
point4 = point2 + point1
print (point3)
print(point4)




