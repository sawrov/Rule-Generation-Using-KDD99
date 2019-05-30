


from random import randint
from DNA import DNA
from numpy import interp
import math

class population:

	population=list()
	average_fitness=0.00
	matingpool=[]
	mutation_rate=0
	min_fitness=0
	max_fitness=0

	def __init__(self, popsize=5,maxstring=5,mutation_rate=0.1):
		self.popsize = popsize
		self.maxstring = maxstring
		self.mutation_rate=mutation_rate

	

	def initialize_population(self):
		for i in range(0,self.popsize):
			self.population.append(DNA(self.maxstring))
	



	def initialize_matingpool(self,min,max):
		self.matingpool=[]
		for individual in self.population:
			freq=int(math.ceil(interp(individual.fitness,[min,max],[1,100])))
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

	def calc_avg_fitness(self):

		for individual in self.population:
			if individual.fitness<self.min_fitness:
				self.min_fitness=individual.fitness
			if individual.fitness>self.max_fitness:
				self.max_fitness=individual.fitness
			self.average_fitness+=individual.fitness

		self.average_fitness=self.average_fitness/self.popsize
		print(self.average_fitness)

#first arg: number of initial population
#second arg: number of bits in a single rule.
#for dna in new.population:
#print(dna.genes)
