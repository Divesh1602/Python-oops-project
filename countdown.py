
class Counter:
	value=0

	def inc(self):
		self.value+=1
		print(self.value)

	def dec(self):
		self.value-=1
		print(self.value)

	def incby(self,n):
		self.value+=n
		print(self.value)

	def decby(self,n):
		self.value-=n
		print(self.value)



value=Counter()
value.inc()
value.dec()

value.incby(5)
value.decby(8)