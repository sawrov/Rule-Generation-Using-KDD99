from Evolution import population
from Preprocessing import process
import numpy as num
from datetime import datetime


new_population =population(10,30)
new_population.initialize()
new_population.calculate_fitness()
best_population=new_population

def show_info(test):
	print test.genes
	print test.fitness
	
era=10
for generation in range(0,era):
	print("-----------------------------------")
	print("Generation: "+str(generation))
	current_population=new_population
	current_population.initialize_matingpool()
	new_population.population=current_population.reproduce()
	new_population.clean_generation()
	new_population.calculate_fitness()
	if best_population.average_fitness<new_population.average_fitness:
		best_population=new_population
	map(show_info,new_population.population)


	print("Average_Fitness:"+str(new_population.average_fitness))


filename= str(datetime.now())
info1="Results/"+filename+"Best_Results.txt"
info2="Results/"+filename+"Constraints.txt"
file=open(info1,"a")
file2=open(info2,"a")
file3=open("Results/recent.txt","w")

ruleset=[]
for individual in best_population.population:
	rule=(" ".join(map(str,individual.genes)))
	ruleset.append(rule)



file.write("\n".join(ruleset))
file2.write("\n Average Fitness: "+str(best_population.average_fitness))
file2.write("\n Total Number of Generation Run: "+str(era))
file2.write("\n Max Fitness: "+str(best_population.max_fitness))
file2.write("\n Min Fitness: "+str(best_population.min_fitness))
file3.write(str(info1))

file.close()
file2.close()



#safal testlai maile bhaneko thiyee ta ho nee ra