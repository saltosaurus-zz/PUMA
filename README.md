# PUMA

##Probably Über Movie Advice

### REQUIREMENTS

#### MySQLdb
These scripts require MySQLdb to be installed on the machine you're attempting to execute them on.  They also require some mucking about with paths, however I have included code to do this for you. 


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