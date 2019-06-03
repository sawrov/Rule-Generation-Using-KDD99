from Preprocessing import process

load_test_data=process(source="KDDTest+.txt")
load_test_data.extract_info()

file="Results/Best_Results.txt"
test_data=[]
print(len(load_test_data.genotype[1]))
print(load_test_data.genotype[1])
with open(file) as fp:
    line=fp.readline()
    while line:
            data=line.split('\n')[0].split(' ')
            if (line != 'EndOfPopulation'):
                test_data.append(map(int,data))
            line=fp.readline()


print(len(test_data))
print(load_test_data.genotype[1][len(test_data[0])])

def isanattack(individual):
    global test_data
    for data in test_data:
        flag = 1
        for i in range(0,len(data)):
		    if(str(data[i])!= str(individual[i])):
			    flag=0
        if(flag==1):
            return flag
    return flag

for data in load_test_data.genotype:
    pred=isanattack(data)
    print("pred="+str(pred))
    # print("Actual="+str(data[len(test_data[0])]))