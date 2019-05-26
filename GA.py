#GA_IDS
from numpy import interp
import pandas as pd
from Evolution import population


# Read data from the dataset and convert to

global ruleset
phenotype= pd.DataFrame({'A' : []})
def readData():
	global phenotype
	if phenotype.empty:
		protocol=['icmp','tcp','udp']
		service=['http','smtp','finger','domain_u','auth','telnet','ftp','eco_i','ntp_u','ecr_i','other','private','pop_3','ftp_data','rje','time','mtp','link','remote_job','gopher','ssh','name','whois','domain','login','imap4','daytime','ctf','nntp','shell','IRC','nnsp','http_443','exec','printer','efs','courier','uucp','klogin','kshell','echo','discard','systat','supdup','iso_tsap','hostnames','csnet_ns','pop_2','sunrpc','uucp_path','netbios_ns','netbios_ssn','netbios_dgm','sql_net','vmnet','bgp','Z39_50','ldap','netstat','urh_i','X11','urp_i','pm_dump','tftp_u','tim_i','red_i']
		flag=['flag','SF','S1','REJ','S2','S0','S3','RSTO','RSTR','RSTOS0','OTH','SH']
		result=['normal.','buffer_overflow.','loadmodule.','perl.','neptune.','smurf.','guess_passwd.','pod.','teardrop.','portsweep.','ipsweep.','land.','ftp_write.','back.','imap.','satan.','phf.','nmap.','multihop.','warezmaster.','warezclient.','spy.','rootkit.']
		file =open('features.txt','r')
		col=file.read().split('\n')
		file.close()
		data=[]
		filepath = 'temp'
		with open(filepath) as fp:
			line = fp.readline()
			while line:
				data_array=line.split('\n')[0].split(',')
				data_array[1]=protocol.index(data_array[1])
				data_array[2]=service.index(data_array[2])
				data_array[3]=flag.index(data_array[3])
				data.append(data_array)
				line = fp.readline()
		phenotype= pd.DataFrame(data, columns=col)
	return phenotype




#My fitness function is wrong,its wrong and it's wrong
#calculate the score of each rules based on the difference of bits.

def fitness(this,that):
	similarity_index=0.00
	if len(this) == len(that):
		for i in range(len(this)):
			if(this[i]==that[i]):
				similarity_index=similarity_index+1
	return similarity_index/28

def calculate_fitness(individual):
	global smurf_train
	max_fitness=0
	avgfitness=0
	for individual in population.population:
		individual.fitness=0
		for packet in smurf_train:
			individual.fitness=individual.fitness+fitness(individual.genes,packet)
		if(individual.fitness>max_fitness):
			max_fitness=individual.fitness
		avgfitness=avgfitness+individual.fitness
	return max_fitness



genotype=readData()
smurf=genotype[["src_bytes","rerror_rate","same_srv_rate","srv_serror_rate","srv_rerror_rate","dst_host_srv_count","dst_host_same_srv_rate","dst_host_diff_srv_rate","dst_host_serror_rate","dst_host_srv_serror_rate"]]
smurf_train=[]
instance=[]
for row in smurf.iterrows():
	instance=[]
	for ind,values in enumerate(row[1]):
		binary_rep=("{0:b}".format(int(float(values))))
		if ind==0:
			binary_rep=binary_rep.zfill(10)
		elif ind==5:
			binary_rep=binary_rep.zfill(10)
		binary_rep=list(binary_rep)
		instance.extend(binary_rep)
	instance=map(int,instance)
	smurf_train.append(instance)

new_data=open("smurf_data","w")
for line in smurf_train:
	c=" ".join(map(str,line))
	new_data.write(c+"\n")

new_population =population(50,28)
new_population.initialize_population()
max=calculate_fitness(new_population)
# for individual in new_population.population:
# 	print individual.genes
# 	print individual.fitness
print("-----------------------------------------------------------------------------------")
final_generation=new_population


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


		

# evolution(new_population,0)
# for individual in final_generation.population:
# 	print individual.fitness
# 	print individual.genes



#safal testlai maile bhaneko thiyee ta ho nee ra