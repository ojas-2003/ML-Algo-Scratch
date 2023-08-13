from csv import reader
import random

def load_csv(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset

#String To Float conversion of Columns
def str_to_float(dataset, column):
    cnt=0

    for row in dataset:
        if cnt==0:
            cnt+=1
            continue
        row[column]=float(row[column].strip())
        cnt+=1


# String Column to Integer

def str_to_int(dataset, column):
    class_vals = [row[column] for row in dataset]
    unique = set(class_vals)

    lookup= dict()
    for i , val in enumerate(unique):
        lookup[val]=i
    for row in dataset:
        row[column]=lookup[row[column]]
    return lookup
   
#loading dataset

filename = "../MACHINE LEARNING/scratch algo/dataset/archive/diabetes.csv"
dataset = load_csv(filename)

for i in range(len(dataset[0])):
    str_to_float(dataset, i)

for i in range(len(dataset[0])):
    if(type(dataset[1][i])==str):
        print(i)
        str_to_int(dataset, i)

print(r'\n the file {0} has {1} rows and {2} columns'.format(filename, len(dataset), len(dataset[0])))

# Finding min and max values of each column

def minmax(dataset):
    minimaxi=list()
    for i in range(len(dataset[0])):
        vals = [row[i] for row in dataset]
        mini = min(vals)
        maxi = max(vals)

        minimaxi.append([mini, maxi])
    return minimaxi

dataset = [[50, 30], [20, 90]]
print(dataset)

minimaxi = minmax(dataset)
print(minimaxi)


def normalizedata(dataset):
    for row in dataset:
        for i in range(len(dataset[0])):
            row[i]= (row[i]-minimaxi[i][0])/(minimaxi[i][1] - minimaxi[i][0])
        
normalizedata(dataset)

for i in range(2):
    for j in range(len(dataset[0])):
        print(dataset[i][j], end=" ")
    print('\n')


def column_mean(dataset):
    means = [0 for i in range(len(dataset[0]))]
    for i in range(len(dataset[0])):
        val = [row[i] for row in dataset]
        means[i]= sum(val)/float(len(dataset))
    return means


def train_test_split(dataset, split=0.6):
    train_list = list()
    train_size = split*len(dataset)
    dataset_copy = list(dataset)

    while len(train_list)<train_size:
        index = randrange(len(dataset_copy))
        train_list.append(dataset_copy.pop(index))
    
    return train_list, dataset_copy
