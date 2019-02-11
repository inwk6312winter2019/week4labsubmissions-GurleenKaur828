class Point():
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def __str__(self):
		return f'({self.x},{self.y})'

	def __add__(self,other):
		sum=(self.x+other.x,self.y+other.y)
		return sum

p=Point(3,4)
q=Point(5,6)
print(p+q)

