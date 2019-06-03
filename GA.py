from Evolution import population
from Preprocessing import processing
import numpy as num

best_population=[]
best_average_fitness=0


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

# evolution(new_population,0)
# for individual in new_population.population:
# 	print individual.fitness
# 	print individual.genes

era=100
for generation in range(0,era):
	print("-----------------------------------")
	print("Generation: "+str(generation))
	current_population=new_population
	current_population.initialize_matingpool(new_population.min_fitness,new_population.max_fitness)
	new_population=current_population.reproduce()
	map(fitness,new_population.population)
	avg=new_population.calc_avg_fitness()
	print("Average_Fitness:"+str(avg))
	if avg>best_average_fitness:
		best_population=new_population
		best_average_fitness=avg
	print("Best Fitness:"+str(best_average_fitness))
print("----------------------")
print(best_population.average_fitness)
file=open("Results/Best_Results.txt","a")
file2=open("Results/Constraints.txt","a")
ruleset=[]
for individual in best_population.population:
	rule=(" ".join(map(str,individual.genes)))
	ruleset.append(rule)

file.write("\n".join(ruleset))
file.write("\nEndOfPopulation")
file2.write("\n Average Fitness: "+str(best_population.average_fitness))
file2.write("\n Total Number of Generation Run: "+str(era))
file2.write("\n Total Number of Generation Run: "+str(era))
file2.write("\n Max Fitness: "+str(best_population.max_fitness))
file2.write("\n Min Fitness: "+str(best_population.min_fitness))
file.close()
file2.close()


#safal testlai maile bhaneko thiyee ta ho nee ra