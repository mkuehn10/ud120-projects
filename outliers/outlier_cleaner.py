#!/usr/bin/python

import pprint
def outlierCleaner(predictions, ages, net_worths):
	"""
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
	"""
	
	cleaned_data = []
	error = 0
	for pred, age, net_worth in zip(predictions, ages, net_worths):
		error = abs(net_worth - pred)
		#print net_worth, pred
		#print error
		print type(float(pred))
		cleaned_data.append((float(age), float(net_worth), float(error)))
	#print type(cleaned_data[0])
	cleaned_data = sorted(cleaned_data, key = lambda tup: tup[2])[0:80]
	pprint.pprint(cleaned_data)
	#cleaned_data = []
	return cleaned_data