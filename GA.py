from Evolution import population
from Preprocessing import processing
import numpy as num



def fitness(individual):
	global load_train_data
	global key_index
	TP=0.00
	TN=0.00
	FP=0.00
	FN=0.00
	for specimen in load_train_data.genotype:
		suspicion=predict(individual.genes,specimen)
		prediction=1
		label=specimen[key_index]
		if(prediction == label):
				TP+=suspicion
		else:
				FP+=suspicion
	fitness=TP/load_train_data.intrusion-FP/load_train_data.normal
	individual.fitness=fitness

def predict(individual,specimen):
	flag=1
	suspicion=0
	for i in range(0,len(individual)):
		if(str(individual[i])== str(specimen[i])):
			suspicion+=1

	suspicion=float(suspicion)/len(individual)
	return suspicion

#
# def calculate_fitness(individual):
# 	global smurf_train
# 	max_fitness=0
# 	avgfitness=0
# 	for individual in population.population:
# 		individual.fitness=0
# 		for packet in smurf_train:
# 			individual.fitness=individual.fitness+fitness(individual.genes,packet)
# 		if(individual.fitness>max_fitness):
# 			max_fitness=individual.fitness
# 		avgfitness=avgfitness+individual.fitness
# 	return max_fitness


def evolution(population, generation):
	print("generation"+str(generation))
	new_genration=population
	max_fitness=calculate_fitness(population)
	if generation<100:
		global final_generation
		final_generation=population
		# print final_generation.population[2].fitness
		# print final_generation.population[2].genes
		population.initialize_matingpool(max_fitness)
		new_genration=population.reproduce()
		# print("---GENERATION--"+str(generation))
		# print("--MAX_FITNESS"+str(max_fitness))
	else:
		return

	evolution(new_genration,generation+1)

load_train_data=processing()
load_train_data.extract_info()

key_index=len(load_train_data.genotype[1])-1
new_population =population(20,key_index)
new_population.initialize_population()

map(fitness,new_population.population)
# evolution(new_population,0)
# for individual in new_population.population:
# 	print individual.fitness
# 	print individual.genes

era=20
for generation in range(0,era):
	print("-----------------------------------")
	print("Generation: "+str(generation))
	current_population=new_population
	current_population.initialize_matingpool(new_population.min_fitness,new_population.max_fitness)
	new_population=current_population.reproduce()
	map(fitness,new_population.population)
	new_population.calc_avg_fitness()


#safal testlai maile bhaneko thiyee ta ho nee ra