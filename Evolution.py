


from random import randint
from DNA import DNA
from numpy import interp
from Preprocessing import process
import math

class population:

	population=list()
	average_fitness=0.00
	matingpool=[]
	mutation_rate=0
	min_fitness=0
	max_fitness=0
	train_data=null

	def __init__(self, popsize=5,maxstring=5,mutation_rate=0.01,source="KDDTrain+_20Percent.txt"):
		self.popsize = popsize
		self.maxstring = maxstring
		self.mutation_rate=mutation_rate
		self.test_data=process(source)
		self.test_data.extract_info()

	

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
			child1,child2=partnera.crossover(partnerb)
			child1.mutate(self.mutation_rate)
			child2.mutate(self.mutation_rate)
			next_generation.population[i]=child1
		return next_generation

	def calc_avg_fitness(self):

		for individual in self.population:
			if individual.fitness<self.min_fitness:
				self.min_fitness=individual.fitness
			if individual.fitness>self.max_fitness:
				self.max_fitness=individual.fitness
			self.average_fitness+=individual.fitness

		self.average_fitness=self.average_fitness/self.popsize
		return (self.average_fitness)

	def calculate_population_fitness(self):
		map(self.fitness,self.population)

	def fitness(self,individual):
		global load_train_data
		global key_index
		TP = 0.00
		TN = 0.00
		FP = 0.00
		FN = 0.00
		for specimen in load_train_data.genotype:
			suspicion = self.predict(individual.genes, specimen)
			prediction = 1
			label = specimen[key_index]
			if (prediction == label):
				TP += suspicion
			else:
				FP += suspicion
		fitness = TP / load_train_data.intrusion - FP / load_train_data.normal
		individual.fitness = fitness

	def predict(self,individual, specimen):
		flag = 1
		suspicion = 0
		for i in range(0, len(individual)):
			if (str(individual[i]) == str(specimen[i])):
				suspicion += 1

		suspicion = float(suspicion) / len(individual)
		if suspicion == 1:
			print("Bingo")
		return suspicion

#first arg: number of initial population
#second arg: number of bits in a single rule.
#for dna in new.population:
#print(dna.genes)
