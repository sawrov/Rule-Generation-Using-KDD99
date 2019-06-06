from Evolution import population
from Preprocessing import process
import numpy as num
from datetime import datetime


new_population =population(200,30)
new_population.initialize()
new_population.calculate_fitness()
performance=0
best_rules=[]

def show_info(test):
	print "Average fitness of the population:"+str(test.average_fitness)
	print "Max fitness:"+str(test.max_fitness)
	print "Min fitness:"+str(test.min_fitness)
	
era=10
for generation in range(0,era):
	print("-----------------------------------")
	print("Generation: "+str(generation))
	current_population=new_population
	current_population.initialize_matingpool()
	new_population.population=current_population.reproduce()
	if new_population.average_fitness>performance:
		performance=new_population.average_fitness
		best_rules=new_population.population
		print "Elite"+str(performance)
	new_population.clean_generation()
	new_population.calculate_fitness()
	show_info(new_population)
	print("------------------------------------")


	print("Average_Fitness:"+str(new_population.average_fitness))


filename= str(datetime.now())
info1="Results/"+filename+"Best_Results.txt"
info2="Results/"+filename+"Constraints.txt"
file=open(info1,"a")
file2=open(info2,"a")
file3=open("Results/recent.txt","w")

ruleset=[]
for individual in best_rules:
	rule=(" ".join(map(str,individual.genes)))
	ruleset.append(rule)

file.write("\n".join(ruleset))
file2.write("\n Average Fitness: "+str(performance))
file2.write("\n Total Number of Generation Run: "+str(era))
file3.write(str(info1))

file.close()
file2.close()



#safal testlai maile bhaneko thiyee ta ho nee ra