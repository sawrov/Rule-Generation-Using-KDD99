#GA_IDS

import pandas as pd


phenotype= pd.DataFrame({'A' : []})
def readData():
	global phenotype
	if phenotype.empty:
		protocol=['icmp','tcp','udp']
		service=['http','smtp','finger','domain_u','auth','telnet','ftp','eco_i','ntp_u','ecr_i','other','private','pop_3','ftp_data','rje','time','mtp','link','remote_job','gopher','ssh','name','whois','domain','login','imap4','daytime','ctf','nntp','shell','IRC','nnsp','http_443','exec','printer','efs','courier','uucp','klogin','kshell','echo','discard','systat','supdup','iso_tsap','hostnames','csnet_ns','pop_2','sunrpc','uucp_path','netbios_ns','netbios_ssn','netbios_dgm','sql_net','vmnet','bgp','Z39_50','ldap','netstat','urh_i','X11','urp_i','pm_dump','tftp_u','tim_i','red_i']
		flag=['flag','SF','S1','REJ','S2','S0','S3','RSTO','RSTR','RSTOS0','OTH','SH']
		result=['normal.','buffer_overflow.','loadmodule.','perl.','neptune.','smurf.','guess_passwd.','pod.','teardrop.','portsweep.','ipsweep.','land.','ftp_write.','back.','imap.','satan.','phf.','nmap.','multihop.','warezmaster.','warezclient.','spy.','rootkit.']

		#opening the features list and reading 
		#please change the path accordingly
		file =open('features.txt','r')
		col=file.read().split('\n')
		print col
		file.close()
		data=[]


		#opening the dataset, mapping the data to values and adding to data frame
		#please change the path accordingly
		filepath = 'temp'
		with open(filepath) as fp:
			line = fp.readline()
			while line:
				print line
				data_array=line.split('\n')[0].split(',')
				data_array[1]=protocol.index(data_array[1])
				data_array[2]=service.index(data_array[2])
				data_array[3]=flag.index(data_array[3])
				data.append(data_array)
				line = fp.readline()
		phenotype= pd.DataFrame(data, columns=col)
	return phenotype
genotype=readData()
print genotype
