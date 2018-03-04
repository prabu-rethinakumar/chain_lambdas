'''Using Numpy '''
import numpy as nump

Data = nump.genfromtxt("C:\\Users\pprra\PycharmProjects\\NumPyProjects\quality.csv",
                       skip_header=1, delimiter=';')

x, y = Data.shape
print("Number of Rows {}".format(x))
print("Number of Columns {}".format(y))

print("Printing the last column")
print(Data[:, -1])
newmeth = sum(Data[:, -1])/x
print("Quality is : {}".format(newmeth))

''' Using CSV '''
import csv
import pprint

with open("C:\\Users\pprra\PycharmProjects\\NumPyProjects\quality.csv", mode='r') as file:
    Data2 = list(csv.reader(file, delimiter=';'))

qual = [float(item[-1]) for item in Data2[1:]]
pprint.pprint("Quality is : {}".format(sum(qual)/len(qual)))
