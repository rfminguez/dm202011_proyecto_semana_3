import pandas as pd
from datetime import datetime

def to_csv(df, path="output"):
	'''
	input: 	pandas dataframe
			output directory
	output:	saves a CSV file from a dataframe with a filename containing its date
	'''
	file_name = f"{path}/submission_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
	df.to_csv(file_name, index=False)

    
def to_df(df, y_predictions):
	'''
	Formats the dataframe in order to be compatible with the competition.

	input:
	- df: dataframe with features with the ids.
	- y_predictions: series with the predictions to send to the competition.

	both df and y_predictions must have the same number of rows.
	'''
	return pd.DataFrame({'id': df['id'], 'price': y_predictions})

