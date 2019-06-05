


from random import randint
from DNA import DNA
from numpy import interp
from Preprocessing import process
import math

class population:

	population=list()
	intermediate_pop=list()
	performance=0.00
	matingpool=[]
	mutation_rate=0.01
	min_fitness=0
	max_fitness=0
	train_data=None
	source=""
	average_fitness=0
	popsize=0   
	total=0                                                                                                  

	def __init__(self, popsize=5,maxstring=5,mutation_rate=0.01,source="KDDTrain+_20Percent.txt"):
		self.popsize = popsize
		self.mutation_rate=mutation_rate
		self.source=source



	

	def initialize(self):
		if not self.train_data:
			self.train_data=process(self.source)
			self.train_data.extract_info()
			self.maxstring = len(self.train_data.genotype[0])
			self.total=self.train_data.intrusion+self.train_data.normal
		for i in range(0,self.popsize):
			self.population.append(DNA(self.maxstring))


	def initialize_matingpool(self):
		self.matingpool=[]
		for individual in self.population:
			freq=int(math.ceil(interp(individual.fitness,[self.min_fitness,self.max_fitness],[1,100])))
			for i in range(0,freq):
				self.matingpool.append(individual)


	def reproduce(self):
		while len(self.intermediate_pop)<self.popsize:
			partnera=self.tournament()
			partnerb=self.tournament()
			child1,child2=partnera.crossover(partnerb)
			child1.mutate(self.mutation_rate)
			child2.mutate(self.mutation_rate)
			self.intermediate_pop.append(partnera)
			self.intermediate_pop.append(partnerb)
			self.intermediate_pop.append(child1)
			self.intermediate_pop.append(child2)

		return self.intermediate_pop[0:self.popsize]
	def tournament(self):
		index=len(self.matingpool)-1
		players=[]
		while len(players) < 3:
			a=randint(0,index)
			element=self.matingpool[a]
			if element not in players:
				players.append(element)
		else:
			if(players[0].fitness>players[1].fitness):
				if(players[0].fitness>players[2].fitness):
					return players[0]
				else:
					return players[2]

			elif players[1]>players[2]:
				return players[1]
			else:
				return players[2]



	def calculate_fitness(self):
		map(self.fitness,self.population)
		avg=0
		min=1
		max=0
		for individual in self.population:
			if(individual.fitness<min):
				min=individual.fitness
			if(individual.fitness>max):
				max=individual.fitness
			avg=avg+individual.fitness
		self.min_fitness=min
		self.max_fitness=max
		self.average_fitness=avg/self.popsize


	def fitness(self,individual):
		a=0.00
		b=0.00

		for specimen in self.train_data.genotype:
			prediction = self.predict(individual.genes, specimen)
			label=specimen[-1]
			if(prediction==1):
				if(label==1):
					a=a+1
				else:
					b=b+1
		fitness=a/self.train_data.intrusion - b/self.train_data.normal
		individual.fitness = fitness



	def predict(self,individual, specimen):
		
		similarity=0
		limit=len(individual)-1
		for i in range(0, limit-1):
			if (str(individual[i]) == str(specimen[i])):
				similarity=similarity+1
		
		if similarity==limit:
			return individual[-1]
		else:
			return -1

	def clean_generation(self):
		self.intermediate_pop=list()
		self.min_fitness=0
		self.max_fitness=0
		self.average_fitness=0
	

#first arg: number of initial population
#second arg: number of bits in a single rule.
#for dna in new.population:
#print(dna.genes)
