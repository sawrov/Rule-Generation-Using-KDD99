from Preprocessing import process

test=process(source="KDDTest+.txt")
test.extract_info()

def predict(individual, specimen):

        w1=0.239
        w2=0.181
        w3=0.215
        w4=0.162
        w5=0.069
        w6=0.064
        w7=0.055
        w8=0.015
        outcome=0
        if individual[0:7]==specimen[0:7]:
            outcome+=w1
        if individual[7:17]==specimen[7:17]:
            outcome+=w2
        if individual[17:29]==specimen[17:29]:
            outcome+=w3
        if individual[29:31]==specimen[29:31]:
            outcome+=w4
        if individual[31:35]==specimen[31:35]:
            outcome+=w5
        if individual[35:45]==specimen[35:45]:
            outcome+=w6
        if individual[45:52]==specimen[45:52]:
            outcome+=w7
        if individual[52:53]==specimen[52:53]:
            outcome+=w8
        return outcome

file="Results/Best_Results.txt"
with open("Results/recent.txt") as f:
    file=str(f.readline())
rules=[]
with open(file) as fp:
    line=fp.readline()
    while line:
            data=line.split('\n')[0].split(' ')
            rules.append(map(int,data))
            line=fp.readline()

def isanattack(individual):
    global rules
    for rule in rules:
        outcome=predict(individual,rule)
        if(outcome>0.5):
            if(rule[-1]==1):
                print("Attack")
            else:
                print("notanattack")
            return
        

for data in test.genotype:
    print(data)
    print(data[-2])
    isanattack(data)
    print("------------------")

    # print("Actual="+str(data[len(test_data[0])]))