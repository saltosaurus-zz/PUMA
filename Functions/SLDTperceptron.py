## A single-layer, dual-target perceptron

### INPUT: numAttributes is the number of features we're looking at
  #        Examples is a list of feature vectors
  #        Targets is a list of binary (0 or 1) target values for the given examples

### OUTPUT: A list of weights that has a length equal to numAttributes

import dotProduct

def perceptron(numAttributes, Examples, Targets):
    print "Computing weights..."
    weight = []
    eta = 0.1 # Learning rate
    epsilon = 0.5 # Threshold value
    passNum = 1
    for i in range(numAttributes): # Initialize weights to 0
        weight.append(0.0)
    
    error = 1
    error_count = -1
    iteration = 1
    errors = []
    while error_count < 30: # Until our weights are perfect...
        print "On pass number {0}...".format(passNum)
        passNum += 1
        error_count = 0
        for i in range(len(Examples)): # Go through each example...
            dotProd = dotProduct.dotProduct(Examples[i],weight) # Compute a dot product of the example in question and the current weight vector
            result = dotProd > epsilon # Is the product closer to 1 or 0 and class accordingly
            error = Targets[i] - result # Is the classification wrong?
            if error != 0:
                error_count += 1
                for j in range(len(weight)):
                    weight[j] += eta * error * Examples[i][j] # Update weights if it was wrong
        errors.append([iteration,error_count])
        iteration += 1
        if error_count < 25:
            break

    f = open("../DataFiles/errors.txt",'w+')    # Record the errors
    for value in errors:
        print>>f,value
    f.close()
    return weight
