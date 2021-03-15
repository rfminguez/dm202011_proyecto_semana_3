import numpy as np
from sklearn.metrics import mean_squared_error

def get_rmse(y_test, y_predict):
	'''
	Calculates the RMSE error.

	It is just the squared root of the MSE error but it is not in sqlearn.metrics so I create this function to avoid repeating code in my notebooks.

	input:
	- y_test: set of test labels.
	- y_predict: set of predicted results to compare with the test labels.

	output:
	- RMSE error
	'''
	mse_error = mean_squared_error(y_test, y_predict)
	return np.sqrt(mse_error)

