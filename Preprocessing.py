# from numpy import interp
import pandas as pd

# Read data from the dataset and convert to
class processing:

    phenotype= pd.DataFrame({'A' : []})
    type=None
    data=None
    def __init__(self,type=None,source="/"):
        self.type=type
        self.data=source
        self.readData()


    # this function reads the data and converts everything to integer equivalent
    def readData(self):
        if self.phenotype.empty:
            protocol=['icmp','tcp','udp']
            service=['http','smtp','finger','domain_u','auth','telnet','ftp','eco_i','ntp_u','ecr_i','other','private','pop_3','ftp_data','rje','time','mtp','link','remote_job','gopher','ssh','name','whois','domain','login','imap4','daytime','ctf','nntp','shell','IRC','nnsp','http_443','exec','printer','efs','courier','uucp','klogin','kshell','echo','discard','systat','supdup','iso_tsap','hostnames','csnet_ns','pop_2','sunrpc','uucp_path','netbios_ns','netbios_ssn','netbios_dgm','sql_net','vmnet','bgp','Z39_50','ldap','netstat','urh_i','X11','urp_i','pm_dump','tftp_u','tim_i','red_i']
            flag=['flag','SF','S1','REJ','S2','S0','S3','RSTO','RSTR','RSTOS0','OTH','SH']
            label=['normal.','smurf.','neptuno.','back.','teardrop.','pod.','land.','satan.','ipsweep.','portsweep.','nmap.','warezclient.','guess_passwd.','warezmaster.','imap.','ftp_write.','multihop.','phf.','spy.','buffer_overflow.','rootkit.','loadmodule.','perl.']
            file =open('features.txt','r')
            col=file.read().split('\n')
            file.close()
            data=[]
            file=open('data_reduction/count.txt','r')
            count_index=file.read().split('\n')
            file.close
            filepath = 'temp'
            with open(filepath) as fp:
                line = fp.readline()
                while line:
                    data_array=line.split('\n')[0].split(',')
                    data_array[1]=protocol.index(data_array[1])
                    data_array[2]=service.index(data_array[2])
                    data_array[3]=flag.index(data_array[3])
                    test=label.index(data_array[41])

                    # normal labelled as 0
                    # dos labelled as 1
                    # probe labelled as 2
                    # r2l labelled as 3
                    #u2r as 4
                    if(test<1):
                        # data_array[41]="normal"
                        data_array[41]=0
                    elif(test<7):
                        # data_array[41]="dos"
                        data_array[41]=1

                    elif(test<11):
                        # data_array="probe"
                        data_array[41]=2

                    elif(test<19):
                        # data_array="r2l"
                        data_array[41]=3

                    else:
                        # data_array="u2r"
                        data_array[41]=4

                    data.append(data_array)
                    line = fp.readline()
            self.phenotype= pd.DataFrame(data, columns=col)

    # this function converts the integer representation to binary represenation of data
    def extract_info(self):

        selection=self.phenotype[['duration','src_bytes','dst_host_srv_serror_rate','result']]

        for row in selection.iterrows():
            instance=[]
            normal = []
            dos=[]
            probe=[]
            r2l=[]
            u2r=[]
            for ind, values in enumerate(row[1]):
                if(ind<=41):
                    binary_rep = ("{0:b}".format(int(float(values))))
                    # print str(values)+"is represented by"+str(binary_rep)
                    if ind == 1:
                        binary_rep = binary_rep.zfill(30)
                    elif ind == 4:
                        binary_rep = binary_rep.zfill(3)
                    binary_rep = list(binary_rep)
                    instance.extend(binary_rep)
            print "".join(instance)
                # else:
                #
                #     if(values=="normal"):
                #         normal=map(map(int, instance))
                #     elif(values=="dos"):
                #         normal = map(map(int, instance))
                #     elif (values == "probe"):
                #         probe = map(map(int, instance))
                #     elif (values == "r2l"):
                #         r2l = map(map(int, instance))
                #     else:
                #         u2r = map(map(int, instance))


processing1= processing()
processing1.extract_info()





