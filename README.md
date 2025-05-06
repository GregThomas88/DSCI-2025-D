Repo Structure (see machine learning section for recreating the final project results)

Data
- Open Flights Raw
-- This folder contains all of the of the data sets that were gathered from openflights.org, and are the unedited/uncleaned versions of our data. using the files in here we pre processed them in other locations.
-- This folder also contains the data dictionary we made for the raw data files based on information found from the source website.

- Other data files directly under the data directory are preprocesseed/cleaned data sets that were either utilized in the core project or the individual assignments.


Data Engineering
- Distance.py: This file is the function that will take source and destination information and run them through the Google API in order to return the distance and time values. This function was able to be used in the notebook that is able to create the preprocessed and cleaned data set that we used for our code project, usRoutesClean2.csv

- findRoutes.py: This file is the function that will take in a data set with source and destination data, turn it into a directed network graph and then return the shortest path that exists from a given start and end location. This is useful in finding paths to airports that don't have a direct path from the start to the end.


DS Comp
- This folder contains any files we used / created for the DS competition workshop. Not relevant to the core project.


EDA 
- This folder contains all of our individual working EDA files. 


Machine Learning
- This folder contains all of our individual working machine learning files. It also contains the linearProg.ipynb file which is the core file of our project. 
*****Running this file will give the final results of the project, given that all of the referenced files exist in the repo.*****

Research Models
- This folder contains all of the individual files for our research model assignment.