def model_linear(df, reg, X_train, X_test, y_train, y_test):
    '''Handles the code to train with a Linear Regression, and test our cleaned dataset on.'''
    
    # Training our model.
    reg.fit(X_train, y_train)

    # Displaying score of Training variables.
    print("Linear Training score:", reg.score(X_train, y_train)) 

    # Predicting the 'y' target value (Price).
    y_prediction = reg.predict(X_test)

    # Displaying the score of Testing variables
    print("Linear Testing score:", reg.score(X_test, y_test), '\n')