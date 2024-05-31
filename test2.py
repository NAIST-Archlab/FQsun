import matplotlib.pyplot as plt
# import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

X, y = datasets.load_diabetes(return_X_y=True)
y = (y - np.min(y)) / (np.max(y) - np.min(y))
# Use only one feature
X = X[:, np.newaxis, 2]

# Split the data into training/testing sets
X_train = X[:400]
X_test = X[-10:]

# Split the targets into training/testing sets
y_train = y[:400]
y_test = y[-10:]

feature_matrix = np.hstack((X_train, np.ones((len(X_train), 1))))
theta = np.dot(feature_matrix.T, feature_matrix)
theta = np.linalg.inv(theta)
theta = np.dot(theta, feature_matrix.T)
theta = np.dot(theta, y_train)

test_matrix = np.hstack((X_test, np.ones((len(X_test), 1))))
y_pred_exact = np.dot(test_matrix, theta)
mean_squared_error(y_test, y_pred_exact)

from Qsun.Qcircuit import *
from Qsun.Qgates import *

def circuit(params):
    c = Qubit(1)
    RX(c, 0, params[0])
    RY(c, 0, params[1])
    return c

def output(params):
    c = circuit(params)
    prob = c.probabilities()
    return 1*prob[0] - 1*prob[1]

def predict(x_true, coef_params, intercept_params, boundary=10):
    coef = boundary*output(coef_params)
    intercept = boundary*output(intercept_params)
    return coef*x_true.flatten() + intercept

def errors(x_true, y_true, coef_params, intercept_params, boundary):
    return mean_squared_error(y_true, predict(x_true, coef_params, intercept_params, boundary))

def grad(x_true, y_true, coef_params, intercept_params, shift, eta, boundary):
    
    coef_diff = np.zeros((2,))
    intercept_diff = np.zeros((2,))
    start = time.time()
    for i in range(len(coef_params)):
        coef_params_1 = coef_params.copy()
        coef_params_2 = coef_params.copy()
        coef_params_1[i] += shift
        coef_params_2[i] -= shift
        
        for x, y in zip(x_true, y_true):
            coef_diff[i] -= x*(y-predict(x, coef_params, intercept_params, boundary))*(output(coef_params_1)-output(coef_params_2))/(2*np.sin(shift))
        
        
    for i in range(len(coef_params)):
        intercept_params_1 = intercept_params.copy()
        intercept_params_2 = intercept_params.copy()
        intercept_params_1[i] += shift
        intercept_params_2[i] -= shift
        for x, y in zip(x_true, y_true):
            intercept_diff[i] -= (y-predict(x, coef_params, intercept_params, boundary))*(output(intercept_params_1)-output(intercept_params_2))/(2*np.sin(shift))
    print("Time for layers:", time.time()-start)
    coef_diff = coef_diff*boundary*2/len(y_true)
    intercept_diff = intercept_diff*boundary*2/len(y_true)
    
    for i in range(len(coef_params)):
        coef_params[i] = coef_params[i] - eta*coef_diff[i]
        
    for i in range(len(intercept_params)):
        intercept_params[i] = intercept_params[i] - eta*intercept_diff[i]
        
    return coef_params, intercept_params

# # before training
coef_params = np.array([-1.03295171, -0.64020581])
intercept_params = np.array([ 0.84085179, -0.5721947 ])

import time
start = time.time()
costs_train_qlr = []
costs_test_qlr = []
for i in range(5):
    coef_params, intercept_params = grad(X_train, y_train, coef_params, intercept_params, np.pi/20, eta=0.1, boundary=10)
#     costs_train_qlr.append(errors(X_train, y_train, coef_params, intercept_params, boundary))
#     costs_test_qlr.append(errors(X_test, y_test, coef_params, intercept_params, boundary))
end = time.time()

print("Sum:", end-start)
print