def model_boost(df, xg, X_train, X_test, y_train, y_test):
    '''Handles the code to train with a Linear Regression, and test our cleaned dataset on.'''
    
    # Attempt at using XGBoost

    xg.fit(X_train, y_train)
    predictions = xg.predict(X_test)
    print('XGBoost Training score:', xg.score(X_train, y_train))
    print('XGBoost Testing score:', xg.score(X_test, y_test), '\n')