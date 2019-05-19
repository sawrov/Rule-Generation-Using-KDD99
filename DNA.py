from random import randint

class DNA:
	"""docstring for DNA"""
	def __init__(self, maxsize):
		self.genes=[]
		self.fitness=0
		self.size=maxsize
		for i in range(0,self.size):
			self.genes.append(randint(0,1))


	def mutate(self,mutationrate):
		print mutationrate

	def crossover(self, partner):
		midpoint=randint(0,self.size)
		child=DNA(self.size)
		for i in range(0,self.size):
			if i<midpoint:
				child.genes[i]=self.genes[i]
			else:
				child.genes[i]=partner.genes[i]
		return child		
		





		