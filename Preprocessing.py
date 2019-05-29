# from numpy import interp
import pandas as pd

# Read data from the dataset and convert to
class processing:

    phenotype= pd.DataFrame({'A' : []})
    type=None
    data=None
    genotype=[]
    intrusion=0
    normal=0

    def __init__(self,type=None,source="/"):
        self.type=type
        self.data=source
        self.readData()

    # this function reads the data and converts everything to integer equivalent
    def readData(self):
        if self.phenotype.empty:
            protocol=['icmp','tcp','udp']
            flag=['flag','SF','S1','REJ','S2','S0','S3','RSTO','RSTR','RSTOS0','OTH','SH']
            file =open('features.txt','r')
            col=file.read().split('\n')
            file.close()
            data=[]

            file = open('index_files/services.txt', 'r')
            service = file.read().split('\n')
            file.close()

            file=open('index_files/count.txt','r')
            count_index=file.read().split('\n')
            file.close()

            file = open('index_files/dst_bytes.txt', 'r')
            dst_bytes = file.read().split('\n')
            file.close()

            file = open('index_files/duration.txt', 'r')
            duration = file.read().split('\n')
            file.close()

            file = open('index_files/num_compromised.txt', 'r')
            num_compromised = file.read().split('\n')
            file.close()

            file = open('index_files/src_bytes.txt', 'r')
            src_bytes = file.read().split('\n')
            file.close()

            file = open('index_files/srv_count.txt', 'r')
            srv_count = file.read().split('\n')
            file.close()

            file = open('index_files/dst_srv_serror_rate.txt', 'r')
            dst_host_srv_serror_rate = file.read().split('\n')
            file.close()

            file = open('index_files/attack.txt', 'r')
            attack = file.read().split('\n')
            file.close()


            # filepath = 'KDDTrain+.txt'
            # filepath = 'KDDTest+.txt'
            filepath = 'KDDTrain+_20Percent.txt'
            # filepath = 'temp'

            notthere_duration=[]
            notthere_src_bytes=[]
            notthere_dst=[]
            notthere_num_comp=[]
            notthere_count_index=[]
            notthere_srv_count=[]
            notthere_dst_srv_error_rate=[]
            notthere_service=[]
            notthere_attack=[]

            with open(filepath) as fp:
                line = fp.readline()
                while line:
                    data_array=line.split('\n')[0].split(',')

                    if(data_array[0] in duration):
                        data_array[0]=duration.index(data_array[0])
                    else:
                        if data_array[0] not in notthere_duration:
                            notthere_duration.append(data_array[0])


                    data_array[1]=protocol.index(data_array[1])

                    if (data_array[2] in service):
                        data_array[2] = service.index(data_array[2])
                    else:
                        if data_array[2] not in notthere_service:
                            notthere_service.append(data_array[2])


                    data_array[3]=flag.index(data_array[3])

                    if(data_array[4] in src_bytes):
                        data_array[4]=src_bytes.index(data_array[4])
                    else:
                        if data_array[4] not in notthere_src_bytes:
                            notthere_src_bytes.append(data_array[4])

                    if(data_array[5] in dst_bytes):
                        data_array[5]=dst_bytes.index(data_array[5])
                    else:
                        if data_array[5] not in notthere_dst:
                            notthere_dst.append(data_array[5])

                    if data_array[12] in num_compromised:
                        data_array[12]=num_compromised.index(data_array[12])
                    else:
                        if data_array[12] not in notthere_num_comp:
                            notthere_num_comp.append(data_array[12])

                    if data_array[22] in count_index:
                        data_array[22]=count_index.index(data_array[22])
                    else:
                        if data_array[22] not in notthere_count_index:
                            notthere_count_index.append(data_array[22])

                    if data_array[23] in srv_count:
                        data_array[23]=srv_count.index(data_array[23])
                    else:
                        if data_array[23] not in notthere_srv_count:
                            notthere_srv_count.append(data_array[23])


                    if (data_array[38] in dst_host_srv_serror_rate):
                        data_array[38]=dst_host_srv_serror_rate.index(data_array[38])
                    else:
                        if data_array[38] not in notthere_dst_srv_error_rate:
                            notthere_dst_srv_error_rate.append(data_array[38])


                    if(data_array[41] in attack):
                        data_array[41]=attack.index(data_array[41])
                    else:
                        if data_array[41] not in notthere_attack:
                            notthere_attack.append(data_array[41])


                    if(data_array[41]!=0):
                        self.intrusion+=1
                        data_array[41]=1
                    else:
                        self.normal+=1



                            # Code snippet below to classify attacks
                            # normal labelled as 0
                            # dos labelled as 1
                            # probe labelled as 2
                            # r2l labelled as 3
                            # u2r as 4
                            # if(test<1):
                            #     # data_array[41]="normal"
                            #     data_array[41]=0
                            # # elif(test<7):
                            # #     # data_array[41]="dos"
                            # #     data_array[41]=1
                            # #
                            # # elif(test<11):
                            # #     # data_array="probe"
                            # #     data_array[41]=1
                            # #
                            # # elif(test<19):
                            # #     # data_array="r2l"
                            # #     data_array[41]=3
                            #
                            # else:
                            #     # data_array="u2r"
                            #     data_array[41]=1


                    data.append(data_array)
                    line = fp.readline()
            self.phenotype= pd.DataFrame(data, columns=col)
        print("Values below should always be 0, if not index needs to be updated")
        print("-------------------------------------")
        print(len(notthere_duration))
        print(len(notthere_src_bytes))
        print(len(notthere_dst))
        print(len(notthere_num_comp))
        print(len(notthere_srv_count))
        print(len(notthere_dst_srv_error_rate))
        print(len(notthere_count_index))
        print(len(notthere_service))
        print(len(notthere_attack))
        print("-------------------------------------")

        #  Use this code snippet to append any new data to indexes
        # file=open("index_files/dst_bytes.txt",'a')
        # file.write("\n")
        # file.write("\n".join(notthere_dst))
        # file.close()



    # this function converts the integer representation to binary represenation of data
    def extract_info(self):

        selection=self.phenotype[['duration','src_bytes','dst_host_srv_serror_rate','result']]
        print("Extracting Information")

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
                    if ind == 0:
                        binary_rep = binary_rep.zfill(12)
                    elif ind == 1:
                        binary_rep = binary_rep.zfill(12)
                    elif ind == 2:
                        binary_rep = binary_rep.zfill(7)
                    binary_rep = list(binary_rep)
                    instance.extend(binary_rep)
            self.genotype.append(map(int,instance))
    print("Extracting Information Completed")

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




