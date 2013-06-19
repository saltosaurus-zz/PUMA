## Computes a dot product

### INPUT: vals is a list of values (the first element in the dot product)
  #        weights is the weight vector generated from the perceptron (the second element in the dot product)

### OUTPUT: The dot product, a number.

def dotProduct(vals,weights): # Computes a dot product
    sum = 0
    for i in range(len(vals)):
        sum += vals[i] * weights[i]
    return sum
