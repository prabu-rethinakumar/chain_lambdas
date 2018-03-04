import numpy as nump

# Random
data = nump.random.rand(2, 2)
print(data)

# Zeroes
data2 = nump.zeros(shape=(2, 2), dtype=int)
print(data2)

# A range
data3 = nump.arange(10, dtype=int)

# Write to file
filename = 'f.txt'
data3.tofile(filename, sep=';')
f = open(filename, mode='r')
for line in f :
    print(line)

# Read from file
data4 = nump.fromfile(filename, dtype=int, sep=';', count=-1)
print(data4)