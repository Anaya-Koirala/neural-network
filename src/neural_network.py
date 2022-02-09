from functions import * 



W1,b1,W2,b2=gradient_descent(X_train, Y_train, 1 , 150)
dev=print(test_prediction(1, W1, b1, W2, b2))
