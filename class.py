class Athlete:
	def __init__(self,value=0):
		self.thing = value
	def how_big(self):
		return(len(self.thing))
d = Athlete("I love LeiLei")
print(d)
print(str(d))
print d.thing
print d.how_big()
print str(d.how_big())
