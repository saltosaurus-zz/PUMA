## Creates a vector the same length as the number of actors wth each value initialized to 0

### INPUT: numActors is the number of actors (features) total we need to worry about

### OUTPUT: A list of length numActors containing all 0's

def genVect(numActors):
    all_actors_vector = []
    for i in range(numActors):
        all_actors_vector.append(0)
    return all_actors_vector