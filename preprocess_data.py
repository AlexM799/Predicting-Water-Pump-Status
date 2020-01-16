def preprocess_data_for_ML(df_ml, dataset_type, process_options):
"""df_raw: dataset to preprocess
   dataset_type: text describing dataset
   process_options: text indicating steps to/not perform

   return processed dataset
"""
	# change the categorical target feature to numeric and encode
	
	# create numeric values for categorical entries in features
	if dataset_type == 'low_var':
	    combined['basin'] = pd.factorize(combined['basin'])[0]
	    combined['extraction_type_class'] = pd.factorize(combined['extraction_type_class'])[0]
	    combined['management_group'] = pd.factorize(combined['management_group'])[0]
	    combined['payment_type'] = pd.factorize(combined['payment_type'])[0]
	    combined['quantity'] = pd.factorize(combined['quantity'])[0]
	    combined['region'] = pd.factorize(combined['region'])[0]
	    combined['source'] = pd.factorize(combined['source'])[0]
	    combined['waterpoint_type'] = pd.factorize(combined['waterpoint_type'])[0]

	if dataset_type == 'high_var':

 'extraction_type_group',
 'gps_height',
 'id',
 'latitude',
 'longitude',
 'management_group',
 'payment_type',
 'permit',
 'quantity',
 'region_code',
 'source',
 'status_group',
 'waterpoint_type']

