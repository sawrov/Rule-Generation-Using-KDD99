


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
	w1=0.2
	w2=0.8 
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
		for i in range(0,self.popsize):
			a=randint(0,len(self.matingpool)-1)
			b=randint(0,len(self.matingpool)-1)
			partnera=self.matingpool[a]
			partnerb=self.matingpool[b]
			child1,child2=partnera.crossover(partnerb)
			child1.mutate(self.mutation_rate)
			child2.mutate(self.mutation_rate)
			self.intermediate_pop.append(child1)
		return self.intermediate_pop


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
		AB=0
		A=0

		for specimen in self.train_data.genotype:
			prediction = self.predict(individual.genes, specimen)
			if (prediction == "AB"):
				AB += 1
			elif(prediction == "A"):
				A += 1  
		support=AB/self.total
		if(A==0):
			A=1
		confidence = AB/A
		fitness = self.w1*support+self.w2*confidence
		individual.fitness = fitness


	def predict(self,individual, specimen):
		
		condition=1
		result=1
		limit=len(individual)-1
		for i in range(0, limit-1):
			if (str(individual[i]) != str(specimen[i])):
				condition =0
				break;
		this=len(individual)
		if(individual[limit]!=specimen[limit]):
			result=0

		if condition==1 and result == 1:
			return "AB"
		elif condition==1 and result==0:
			return "A"
		else:
			return
	def clean_generation(self):
		self.intermediate_pop=list()
		self.min_fitness=0
		self.max_fitness=0
		self.average_fitness=0
	

#first arg: number of initial population
#second arg: number of bits in a single rule.
#for dna in new.population:
#print(dna.genes)
