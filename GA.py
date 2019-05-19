#GA_IDS
from numpy import interp
import pandas as pd
from Evolution import population


# Read data from the dataset and convert to


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




#calculate the score of each rules based on the difference of bits.
def calculate_fitness(this,that):
	similarity_index=0.00
	if len(this) == len(that):
		for i in range(len(this)):
			if(this[i]==that[i]):
				similarity_index=similarity_index+1
	return similarity_index/28




genotype=readData()
smurf=genotype[["src_bytes","rerror_rate","same_srv_rate","srv_serror_rate","srv_rerror_rate","dst_host_srv_count","dst_host_same_srv_rate","dst_host_diff_srv_rate","dst_host_serror_rate","dst_host_srv_serror_rate"]]
smurf_test_cases=[]
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
	smurf_test_cases.append(instance)
#


current_generation =population(100,28)
current_generation.initialize_population()

max_fitness=0
for individual in current_generation.population:
		for packet in smurf_test_cases:
			individual.fitness=individual.fitness+calculate_fitness(individual.genes,packet)
		if(individual.fitness>max_fitness):
			max_fitness=individual.fitness


# for individual in current_generation.population:
	# print individual.fitness


current_generation.initialize_matingpool(max_fitness)
next_generation=current_generation.reproduce()
for individual in next_generation.population:
	print individual.genes

#safal testlai maile bhaneko thiyee ta ho nee ra