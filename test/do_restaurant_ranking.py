import numpy as np

# Функция для обучения линейной регрессии
def get_weights_linear_regression(features, labels):
    # Добавление столбца единиц для свободного члена регрессии (b0)
    x = np.c_[np.ones(features.shape[0]), features]
    # Решение нормального уравнения для получения весов (b)
    weights = np.linalg.inv(x.T @ x) @ x.T @ labels
    return weights

# Предсказание значений целевых переменных y
def predict_linear_regression(features, weights):
    x = np.c_[np.ones(features.shape[0]), features]
    predictions = x @ weights
    return predictions

restaurants = np.array([
    [4.5, 2.0, 3.0, 5.0],
    [3.0, 3.5, 4.0, 4.0],
    [5.0, 2.0, 4.0, 4.5],
    [4.0, 3.0, 3.5, 4.0],
    [4.5, 3.0, 2.5, 5.0],
])

# Метки (любые, например представляющие рейтинг)
ratings = np.array([5, 3, 4, 2, 4])

# Обучение модели линейной регрессии
weights = get_weights_linear_regression(restaurants, ratings)

# Предсказание рейтингов
predicted_ratings = predict_linear_regression(restaurants, weights)

# Ранжирование ресторанов на основе предсказанного рейтинга
ranking_indices = np.argsort(-predicted_ratings)
print(ranking_indices)