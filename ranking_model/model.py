import numpy as np

from fastapi import APIRouter, Request


router = APIRouter()


def _data_normalization(x):
    x_mean = np.mean(x, axis=0)
    x_std = np.std(x, axis=0)
    x_std += 1e-10

    x_normalized = (x - x_mean) / x_std
    x_normalized = np.hstack((np.ones((x_normalized.shape[0], 1)), x_normalized))

    return x_normalized

def _predict_linear_regression(x, weights):
    return x.dot(weights)

@router.post("/learning")
async def learn_linear_regression(request: Request):
    data = await request.json()

    assert "x" in data
    assert "y" in data
    assert "weights" in data

    x = np.array(data["x"], dtype=np.float64)
    y = np.array(data["y"], dtype=np.float64)
    weights = np.array(data["weights"], dtype=np.float64)

    x = _data_normalization(x)

    for _ in range(20):
        predictions = _predict_linear_regression(x, weights)
        errors = predictions - y
        gradient = (2.0 / (x.size / 4)) * x.T.dot(errors)
        weights -= 0.01 * gradient

    return {"weights": weights.tolist()}

@router.post("/ranking")
async def ranking(request: Request):
    data = await request.json()

    assert "x" in data
    assert "weights" in data

    x = np.array(data["x"], dtype=np.float64)
    weights = np.array(data["weights"], dtype=np.float64)

    x = _data_normalization(x)
    predictions = _predict_linear_regression(x, weights)
    ranked_indices = np.argsort(predictions)[::-1]

    return {"ranked": ranked_indices.tolist()}
