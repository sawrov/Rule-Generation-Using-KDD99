


from random import randint
from DNA import DNA
from numpy import interp
import math

class population:

	population=list()
	fitness=[]
	matingpool=[]
	mutation_rate=0

	def __init__(self, popsize=5,maxstring=5,mutation_rate=0.1):
		self.popsize = popsize
		self.maxstring = maxstring
		self.mutation_rate=mutation_rate

	

	def initialize_population(self):
		for i in range(0,self.popsize):
			self.population.append(DNA(self.maxstring))
	



	def initialize_matingpool(self,max_fitness):		
		self.matingpool=[]
		for individual in self.population:
			freq=int(math.ceil(interp(individual.fitness,[0,max_fitness],[1,100])))
			for i in range(0,freq):
				self.matingpool.append(individual)


	def reproduce(self):
		next_generation=population(self.popsize,self.maxstring,self.mutation_rate)
		for i in range(0,self.popsize):
			a=randint(0,len(self.matingpool)-1)
			b=randint(0,len(self.matingpool)-1)
			partnera=self.matingpool[a]
			partnerb=self.matingpool[b]
			child=partnera.crossover(partnerb)
			child.mutate(self.mutation_rate)
			next_generation.population[i]=child
		return next_generation





#first arg: number of initial population 
#second arg: number of bits in a single rule.
#for dna in new.population:
#print(dna.genes)
