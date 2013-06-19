## Computes error rates for our training data by evaluating prediction performance against 2011/2012 movies

import sys
import os

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Functions/'))
if not path in sys.path:
    sys.path.insert(1, path)
del path

import testError

# Initialize our lists
data_matrix = []
data_targets = []
weights = []
revThreshold = 6.5 # The threshold by which we're determine if a movie is good or bad

# For the test data years, get the data and targets from disk...
for year in [2011,2012]:
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

# Convert the target data to binary targets
binary_targets = []
print "Converting targets..."
for target in data_targets:
    if target > revThreshold:
        binary_targets.append(1)
    else:
        binary_targets.append(0)

# Get the weights
f = open("../DataFiles/weights.txt")
print "Getting weights..."
for line in f:
    weights.append(float(line))
f.close()

# Display the results
print "Testing error: ",
print testError.testError(data_matrix,binary_targets,weights)
