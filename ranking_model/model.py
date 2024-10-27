from fastapi import APIRouter

router = APIRouter()

# Логика ранжирования

import numpy as np

def data_normalization(x):
    x_mean = np.mean(x, axis=0)
    x_std = np.std(x, axis=0)
    x_normalized = (x - x_mean) / x_std
    x_normalized = np.hstack((np.ones((x_normalized.shape[0], 1)), x_normalized))

    return x_normalized

def learn_linear_regression(x, y, weights):
    for iteration in range(20):
        predictions = x.dot(weights)
        errors = predictions - y
        gradient = (2.0 / (x.size / 4)) * x.T.dot(errors)
        weights -= 0.01 * gradient

    return weights

def predict_linear_regression(x, weights):
    predictions = x.dot(weights)
    return predictions

def ranking(x, weights):
    x = data_normalization(x)
    predictions = x.dot(weights)
    ranked_indices = np.argsort(predictions)[::-1]

    return ranked_indices
