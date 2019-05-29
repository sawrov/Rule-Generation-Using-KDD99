from Evolution import population
from Preprocessing import processing



def fitness(individual):
	global load_train_data
	global key_index
	TP=0
	TN=0
	FP=0
	FN=0
	for specimen in load_train_data.genotype:
		prediction=predict(individual.genes,specimen)
		label=specimen[key_index]
		if(prediction == label):
			if(label==1):
				TP+=1
			else:
				TN+=1
		else:
			if(label==1):
				FN+=1
			else:
				FP+=1
	if(TP>0 | FP>0):
		print(TP)
		print(TN)
		print(FP)
		print(FN)









def predict(individual,specimen):
	flag=1
	for i in range(0,len(individual)):
		if(str(individual[i])!= str(specimen[i])):
			flag=0
			break
	return flag

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
print(load_train_data.normal)
print(load_train_data.intrusion)
print(len(load_train_data.genotype[1]))

key_index=len(load_train_data.genotype[1])-1
new_population =population(1000,key_index)
new_population.initialize_population()

map(fitness,new_population.population)
# evolution(new_population,0)
# for individual in final_generation.population:
# 	print individual.fitness
# 	print individual.genes



#safal testlai maile bhaneko thiyee ta ho nee ra