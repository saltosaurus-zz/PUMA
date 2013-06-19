## Computes the testing error for the perceptron

### INPUT: Examples is a list of feature vectors
  #        Targets is a list of target classes
  #        weights is a list of perceptron-generated weights

### OUTPUT: The test error (float)

import dotProduct

def testError(Examples,Targets,weights):
    error = 0.0
    for example, target in zip(Examples, Targets):
        result = dotProduct.dotProduct(example, weights)
        if result > .5:
            result = 1
        else:
            result = 0
        if result != target:
            error += 1
    return error / len(Examples)