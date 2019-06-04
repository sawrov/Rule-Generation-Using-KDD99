from Evolution import population
from Preprocessing import process
import numpy as num

new_population =population(200,30)
new_population.initialize()
new_population.calculate_fitness()

def show_info(test):
	print test.genes
	print test.fitness
	
era=100
for generation in range(0,era):
	print("-----------------------------------")
	print("Generation: "+str(generation))
	current_population=new_population
	current_population.initialize_matingpool()
	new_population.population=current_population.reproduce()
	new_population.clean_generation()
	new_population.calculate_fitness()
	map(show_info,new_population.population)
	print("Average_Fitness:"+str(new_population.average_fitness))







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