import pandas as pd
from datetime import datetime
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix


def create_model(algorithm_name, classifier, dataset_type, X_train_data, X_test_data, y_train_data, y_test_data, tuning_model='None', hyperparams='None'):
    """create a model by fitting the algorithm to the training data
       predict using testing data
       print the confusion matrix & classification report
       store the f1 results to the cumulative results file
       return the model
    """
    t0 = datetime.now()
      
    #if performing hyperparameter tuning & cross validation, use those estimators to fit
    #otherwise use the basic classifier
    if tuning_model == 'Grid':
        estimator = GridSearchCV(classifier, hyperparams, cv=5, verbose=0)
    elif tuning_model == 'Random':
        estimator = RandomizedSearchCV(classifier, hyperparams, n_iter=15, cv=5, verbose=0, random_state=42)
    else:
        estimator = classifier
    
    # Fit the classifier to the data
    model = estimator.fit(X_train_data, y_train_data)

    if tuning_model != 'None':
        print('Best parameters: ', sorted(model.best_params_.items()))
        
    # Predict the labels for the training data X
    y_pred = model.predict(X_test_data)
    
    # Print the confusion matrix and classification report
    print('Confusion maxtrix: \n', confusion_matrix(y_test_data, y_pred))
    print('Classification report: \n', classification_report(y_test_data, y_pred))
    
    run_time = datetime.now() - t0
    print('Run time: ', run_time)
    
    class_report_dict = classification_report(
        y_test_data, y_pred, labels=[0, 1, 2], target_names=['functional', 'non functional', 'needs maintenance'], output_dict=True)
    t0 = datetime.now()
    
       # initialize dataframe to hold results
    columns = ['algorithm', 'data note', 'Func F1', 'Non_Func F1', 'Needs_Maint F1', 'train_acc', 'test_acc', 'run time', 'hyper_params']
    #df = pd.DataFrame(columns=columns)
  
    
    df_results = pd.DataFrame([[
    algorithm_name,
    dataset_type,
    class_report_dict['functional']['f1-score'],
    class_report_dict['non functional']['f1-score'],
    class_report_dict['needs maintenance']['f1-score'],
    model.score(X_train_data, y_train_data),
    model.score(X_test_data, y_test_data),        
    run_time,
    model.get_params()]], columns=columns)
    
    return model, df_results


def factorize_objects(df_to_fact):
    """ input: df_to_fact - pandas dataframe
        returns: pandas dataframe with factorized data
    """
    # get a list of columns names that are of type object
    df_datatypes = pd.DataFrame(df_to_fact.dtypes, columns=['datatype']).reset_index()
    df_datatypes.columns=['feature', 'datatype']
    object_cols = df_datatypes[df_datatypes['datatype']=='object']
    cols = object_cols['feature'].values

    # factorize each object column
    for col in cols:
        df_to_fact[col] = pd.factorize(df_to_fact[col])[0].astype('object')
    
    return df_to_fact





