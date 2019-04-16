from random import randint

class DNA:
	"""docstring for DNA"""
	genes=[]
	fitness=0
	size=10
	def __init__(self, maxsize):
		self.size=maxsize
		for i in range(0,self.size):
			self.genes.append(randint(0,1))


	def getphrase(self):
		print (str(self.genes))

	def calc_fitness(self):
		print self.fitness
		return self.fitness


	def mutate(self):
		print "mutating"

	def crossover(self, DNA):
		print"child"





		