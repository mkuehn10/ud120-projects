#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import pprint

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

pprint.pprint(enron_data.keys())

# How many data points (i.e. people) are in the Enron dataset?
print(len(enron_data.keys()))

poi_count = 0
poi_total_payment_NaN = 0
for key in enron_data.keys():
	#pprint.pprint(enron_data[key].keys())
	# For each person, how many features are available?
	#print len(enron_data[key].keys())
	
	if enron_data[key]['poi'] == True:
		poi_count += 1
		if enron_data[key]['total_payments'] == "NaN":
			poi_total_payment_NaN += 1
	#break

print "POIs",poi_count

for key in enron_data.keys():
	pprint.pprint(enron_data[key].keys())
	# For each person, how many features are available?
	#print len(enron_data[key].keys())
	
	
	break

print enron_data['PRENTICE JAMES']['total_stock_value']
print enron_data['COLWELL WESLEY']['from_this_person_to_poi']
print enron_data['SKILLING JEFFREY K']['exercised_stock_options']

print enron_data['SKILLING JEFFREY K']['total_payments']
print enron_data['LAY KENNETH L']['total_payments']
print enron_data['FASTOW ANDREW S']['total_payments']

salary_count = 0
known_email_count = 0
total_payments_NaN = 0
total_stock_NaN = 0

for key in enron_data.keys():
	if enron_data[key]['salary'] != "NaN":
		salary_count += 1
	if enron_data[key]['email_address'] != "NaN":
		known_email_count += 1
	if enron_data[key]['total_payments'] == "NaN":
		total_payments_NaN += 1
	if enron_data[key]['total_stock_value'] == "NaN":
		total_stock_NaN += 1
	
	#for v in enron_data[key].keys():
		#print enron_data[key][v]
		
	# For each person, how many features are available?
	#print len(enron_data[key].keys())
	
	
	#break
print "Salary Count:", salary_count
print "Email Count:", known_email_count
print "% of Total Payment NaN:", float(total_payments_NaN) / len(enron_data.keys())
print "% of POIs with Total Payment NaN", float(poi_total_payment_NaN) / poi_count
print total_payments_NaN