def run_Pandas_Profiling(working_df, break_into_sections = False, num_cols=5, logging=False):
    """Run Pandas_Profiling 
    """
    t0 = datetime.now()
    start_col_idx = 0
    end_col_idx = num_cols
    cols = list(working_df.columns)
    total_cols = len(cols)
    
    if logging:
        log_entry = str('Pandas Profiling start ' + t0.strftime("%m/%d/%Y, %H:%M:%S"))
        logging.info(log_entry)
    
    if break_into_sections:
        while end_col_idx <= total_cols:
            #slice the column list by the given num_cols
            cols_by_section = cols[start_col_idx:end_col_idx] 

            #make sure the target variable is in the heat maps
            if 'status_group' not in cols_by_section:
                cols_by_section.append('status_group')

            #create a dataset with only the selected columns
            df_to_profile = working_df.loc[:, cols_by_section]
               
            #run the profile
            profile = df_to_profile.profile_report(title = 'Pandas Profiling Report')
            profile.to_file(output_file = timestamp + '_' + str(start_col_idx) + "output.html")

            #update the indicies for the next slice or the end slice
            start_col_idx = end_col_idx 
            if (end_col_idx + num_cols > total_cols) and (total_cols % num_cols > 0):
                end_col_idx += total_cols % num_cols
            else:
                end_col_idx += num_cols
    else:
        #run the profile on all of the columns
        profile = working_df.profile_report(title='Pandas Profiling Report')
        profile.to_file(output_file= timestamp + '_' + str(start_col_idx) + "output.html")

