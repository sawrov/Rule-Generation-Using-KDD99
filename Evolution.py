


from random import randint
from DNA import DNA

class evolution:

	maxpop=100
	maxstring=30
	population=[]
	fitness=[]

	def __init__(self, maxpop,maxstring):
		self.maxpop = maxpop
		self.maxstring = maxstring

	def initialize_population(self):
		for i in range(0,self.maxpop):
			self.temp=[]
			for i in range(0,self.maxstring):
				self.temp.append(randint(0,1))
			self.population.append(self.temp)




#first arg: number of initial population 
#second arg: number of bits in a single rule


rule=DNA(10)
rule.getphrase()