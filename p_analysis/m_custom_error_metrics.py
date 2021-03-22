import numpy as np
from sklearn.metrics import mean_squared_error

def get_average_rmse(scores):
	'''
	Calculates the average RMSE error.

	input:
	- scores: an array with Negative RMSE scores

	output:
	- Average RMSE error
	'''
	return np.mean(-scores)

