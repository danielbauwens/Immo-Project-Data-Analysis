def model_tree(df, dtr, X_train, X_test, y_train, y_test):
    '''Handles the code to train with DecisionTree, and test our cleaned dataset on.
    '''
    dtr.fit(X_train, y_train)
    print('DTR Training score:', dtr.score(X_train, y_train))
    y_pred = dtr.predict(X_test)
    print('DTR Testing score:', dtr.score(X_test, y_test), '\n')