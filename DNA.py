from random import randint
from random import uniform

class DNA:
	"""docstring for DNA"""
	def __init__(self, maxsize):
		self.genes=[]
		self.fitness=0.00
		self.size=maxsize
		for i in range(0,self.size):
			self.genes.append(randint(0,1))


	def mutate(self,mutationrate):
		for i in range(0,self.size):
			if(uniform(0,1)<mutationrate):
				self.genes[i]=randint(0,1)

	def crossover(self, partner):
		midpoint=randint(0,self.size)
		child1=DNA(self.size)
		child2=DNA(self.size)
		for i in range(0,self.size):
			if i<midpoint:
				child1.genes[i]=self.genes[i]
				child2.genes[i]=partner.genes[i]
			else:
				child1.genes[i]=partner.genes[i]
				child2.genes[i]=self.genes[i]
		return child1,child2







		