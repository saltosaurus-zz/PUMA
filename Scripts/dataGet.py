## This script pulls the data from the local database, builds the feature vectors for each movie, and saves it into text files located in ../DataFiles

import sys
import os

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Functions/'))
if not path in sys.path:
    sys.path.insert(1, path)
del path

import MySQLdb
import genVect

## DATABASE CONNECTION DETAILS SHOULD BE BLANK AT COMMIT ##
db = MySQLdb.connect(host="", user="", passwd="",db="IMDB")
cursor = db.cursor()

# Grabs all of the actors within the timeframe we're looking at (2000 - 2010)
cursor.execute("SELECT person_id FROM imdb_distinct_actors")
actors = cursor.fetchall()
numActors = 0
existingActors = []

# We count the number of actors as we append them onto our list of actors
for actor in actors:
    numActors += 1
    existingActors.append(actor[0])

# Initialize the lists we'll use as our makeshift vectors
full_data_matrix = []
data_targets = []

# Cycle through the years getting the data and storing it in our lists
for year in [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012]:
    print "Beginning the processing of {0}...".format(year)
    cursor.execute("SELECT movie_id FROM imdb_movies_{0}".format(year))
    movie_ids = cursor.fetchall()
    
    for row in movie_ids:   # Once we have the movie ids we walk through each movie at look at the actors that were in it
        cursor.execute("Select person_id FROM imdb_actors_{0} where (movie_id = {1})".format(year,row[0]))
        actors = cursor.fetchall()
        movie_vect = genVect.genVect(numActors)
        
        for actor in actors:    # For every actor in the movie in question...
            if actor[0] in existingActors:
                movie_vect[existingActors.index(actor[0])] = 1        
        cursor.execute("Select info from imdb_rating_{0} where movie_id = {1}".format(year,row[0])) # Get it's rating
        rating = cursor.fetchall()
        for thingy in rating:
            full_data_matrix.append(movie_vect)
            data_targets.append(rating[0][0])

    f = open("../DataFiles/data_{0}.txt".format(year),'w+')  # Begin the process of writing all of the data gathered to disk
    for vector in full_data_matrix:
        for element in vector:
            thingy = str(element)
            thingy += ","
            print>>f, thingy,
        print>>f, " "
    f.close()
    full_data_matrix = []

    f = open("../DataFiles/targets_{0}.txt".format(year),'w+')  # Write the class targets to file as the base user review score
    for target in data_targets:
        print>>f, target
    f.close()
    data_targets = []
    print "------------------------------------ {0} Complete ------------------------------------".format(year)

# Finally we store the order of the actors for later use
f = open("../DataFiles/actors.txt",'w+')
for person in existingActors:
    print>>f, person
f.close()



