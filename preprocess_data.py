def preprocess_data_for_ML(df_ml, dataset_type, process_options):
"""df_raw: dataset to preprocess
   dataset_type: text describing dataset
   process_options: text indicating steps to/not perform

   return processed dataset
"""
	# change the categorical target feature to numeric and encode
	label_dict_status_group = {'functional':0,
                   'non functional': 1,
                   'functional needs repair': 2}
	df_ml['status_group'] = df_ml['status_group'].replace(label_dict_status_group)
	
