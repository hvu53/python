class Point:
	def __init__(self, initX, initY):
		self.x = initX
		self.y = initY

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def distanceFromOrigin(self):
		return ((self.x**2) + (self.y**2))**0.5

	def __str__(self):
		return "x =" + str(self.x) + ", y= " + str(self.y)

	def halfway(self, target):
		mx = float(self.getX() + target.getX())/2
		my = float(self.getY() + target.getY())/2
		return Point(mx,my)

	def distanceFromPoint(self, target):
		dx = target.getX() - self.getX()
		dy = target.getY() - self.getY()
		return (dx**2 + dy**2)**0.5

	def reflect_x(self):
		mx = self.getX()
		my = self.getY() * (-1)
		return Point(mx, my)

	def slope_from_origin(self):
		if self.getX() == 0:
			return None
		else:
			return float(self.getY())/float(self.getX())

	def move(self, dx, dy):
		self.x = self.x + dx
		self.y = self.y + dy
p = Point(3,3)
q = Point(6,7)
mid = p.halfway(q)
print mid
print p.distanceFromPoint(q)
print p.reflect_x()
print q.slope_from_origin()

p.move(5,10)
print(p)