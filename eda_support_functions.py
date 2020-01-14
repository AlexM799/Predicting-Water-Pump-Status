
import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency 

def cramers_v(x, y):
	"""inputs: two numeric, nominal values, x and y
	   returns: correlation between x and y using Cramer's V approach
	"""
	confusion_matrix = pd.crosstab(x,y)
	chi2 = chi2_contingency(confusion_matrix)[0]
	n = confusion_matrix.sum().sum()
	phi2 = chi2/n
	r,k = confusion_matrix.shape
	phi2corr = max(0, phi2-((k-1)*(r-1))/(n-1))
	rcorr = r-((r-1)**2)/(n-1)
	kcorr = k-((k-1)**2)/(n-1)
	return np.sqrt(phi2corr/min((kcorr-1),(rcorr-1)))


def create_correlation_matrix(df_to_test):
	"""inputs: pandas dataframe containing numeric data
	   returns: correlation matrix between features in dataframe
	"""

	columns = df_to_test.columns
	corr = pd.DataFrame(index=columns, columns=columns)
	for i in range(0,len(columns)):
		for j in range(i,len(columns)):
			if i == j:
				corr[columns[i]][columns[j]] = 1.0
			else:
				cell = cramers_v(df_to_test[columns[i]], df_to_test[columns[j]])
				corr[columns[i]][columns[j]] = cell
				corr[columns[j]][columns[i]] = cell
	corr.fillna(value=np.nan, inplace=True)
	return corr

def get_feature_correlations(df_to_test, threshold):
	""" inputs: pandas dataframe containing numeric data
		returns: dataframe of correlations greater than threshold between each feature
	"""
	indep_list = []
	cols = df_to_test.columns
	results = np.empty(len(cols))
	for i in range(0,len(columns)):
		for j in range(i,len(columns)):
			if i == j:
				indep_list.append([cols[i], cols[j], 1, 1, 1])
			else:
				result_s = spearmanr(df_to_test[cols[i]], df_to_test[cols[j]])
				result_v = cramers_v(df_to_test[cols[i]], df_to_test[cols[j]])
				confusion_matrix = pd.crosstab(df_to_test[cols[i]],df_to_test[cols[j]])
				chi2_pvalue = chi2_contingency(confusion_matrix)[1]
				indep_list.append([cols[i], cols[j], result_s[0], result_s[1], result_v, chi2_pvalue])
	df_v = pd.DataFrame(indep_list, columns=['feature 1', 'feature 2', 'S correlation', 'S pvalue', 'C-V correlation', 'chi2 pvalue'])
	df_v.sort_values(by=['C-V correlation'], inplace=True, ascending=False)
	df_v = df_v[np.logical_and(df_v['C-V correlation']>threshold, df_v['C-V correlation']<1.0)]
	return df_v
