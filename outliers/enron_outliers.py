#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
import pprint
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop('TOTAL', 0)
#pprint.pprint(data_dict)
for key in data_dict.keys():
    #pprint.pprint(key)
    bonus = data_dict[key]['bonus']
    salary = data_dict[key]['salary']
    if (( bonus > 5000000) and (salary > 1000000) and (bonus != "NaN") and (salary != "NaN")):
        
        print key
        print data_dict[key]['bonus']
        print data_dict[key]['salary']


data = featureFormat(data_dict, features)


### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
