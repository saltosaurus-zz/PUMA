##  This script runs the data through the perceptron to generate the weights.  It then dumps these values to text files.

import sys
import os

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Functions/'))
if not path in sys.path:
    sys.path.insert(1, path)
del path

import SLDTperceptron

#  Access the actors
f = open("../DataFiles/actors.txt")
existingActors = []
for actor in f:
    existingActors.append(int(actor))
f.close()

# How many actors are there?
numActors = len(existingActors)

# Initialize the lists to be used
data_matrix = []
data_targets = []
revThreshold = 6.5

# Cycle through the years we're using as our training data and pull it in
for year in [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010]:
    print "Importing data for {0}...".format(year)
    f = open("../DataFiles/data_{0}.txt".format(year))
    for line in f:
        data = line.split(',')
        data_matrix.append([int(x) for x in data[:len(data)-1]])
    f.close()
    f = open("../DataFiles/targets_{0}.txt".format(year))
    for line in f:
        data_targets.append(float(line))
    f.close()

# Convert the target data into binary targets for the perceptron
binary_targets = []
print "Converting targets..."
for target in data_targets:
    if target > revThreshold:
        binary_targets.append(1)
    else:
        binary_targets.append(0)

# Call the perceptron and get the weight vector for our training data
weights = SLDTperceptron.perceptron(numActors, data_matrix, binary_targets)

# Save our weight vector to disk
f = open("../DataFiles/weights.txt",'w+')
for weight in weights:
    print>>f, weight
f.close()