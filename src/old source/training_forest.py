def model_forest(df, rforest, X_train, X_test, y_train, y_test):
    '''Handles the code to train with RandomForest regressor, and test our cleaned dataset on.
    '''

    rforest.fit(X_train, y_train)
    prd = rforest.predict(X_test)
    print('RandomForest Training score:', rforest.score(X_train, y_train))
    print('RandomForest Testing score:', rforest.score(X_test, y_test), '\n')