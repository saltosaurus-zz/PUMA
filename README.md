# PÜMA

##Probably Über Movie Advice

### REQUIREMENTS

#### MySQLdb
The scripts require MySQLdb to be installed on the machine you're attempting to execute them on.  They also require some mucking about with paths, however I have included code to do this for you. 

#### IMDB Data
The scripts assume you have access to a local copy of the IMDB databases.  This can be pulled using a variety of methods.  We used IMDBpy.  Secondly we modified the resultant database heavily as described in the wiki.


### STRUCTURE

#### DataFiles
This folder contains all of the generated data files from running the scripts.  DO NOT modify these directly.  If there is a need to change the data, delete them and generate new ones.

#### Functions
This folder contains all of the functions to be used by the scripts, including most importantly, the perceptrons.  Modify these at your own peril (doing so may break the scripts).

#### Scripts
This folder contains the three scripts used in the generation and manipulation of the data.  They are as follows:

##### dataGet.py
Contacts the database and pulls the actor and target data.  It then manipulates this data to generate a set of feature vectors in a list.  Finally, it writes both the feature vectors and the target data to files within DataFiles.

##### compWeights.py
Pulls in the data from dataGet and runs the feature vectors through the perceptron (currently only the SLDT perceptron).  Once it's computed weights it writes these to files within DataFiles.

##### doTests.py
Takes the weights and the test data (movie information from 2011 and 2012) and computes the prediction performance.


### USAGE

To use the scripts, you must first modify the following line:
	db = MySQLdb.connect(host="", user="", passwd="",db="IMDB")
Add your host, username and password to the IMDB database copy you are using.  At the command line, enter:

	python dataGet.py

This will execute the data gathering script.  Once this has completed, enter:

	python compWeight.py

This will run the data through the perceptron, computing the resultant weights.  Once you have the weights, determine the prediction error by entering:

	python doTests.py