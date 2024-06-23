import numpy as np

def smape(y_true: np.array, y_pred: np.array) -> float:
    """
    Вычисляет Symmetric Mean Absolute Percentage Error (SMAPE) между двуми массивами.

    SMAPE - это мера точности, основанная на процентных различиях между двумя временными рядами.
    Он вычисляется как среднее значение абсолютных процентных ошибок.

    Параметры:
    y_true (np.array): Массив истинных (фактических) значений.
    y_pred (np.array): Массив предсказанных значений.

    Возвращает:
    smape_value (float): Значение SMAPE между y_true и y_pred.

    Примечания:
    Если и y_true, и y_pred равны нулю, SMAPE определяется как 0.
    """
    denominator = np.abs(y_true) + np.abs(y_pred)
    non_zero_denominator = denominator != 0
    safe_denominator = denominator.copy()
    safe_denominator[~non_zero_denominator] = 1
    smape_value = 2 * np.abs(y_true - y_pred) / safe_denominator
    smape_value[~non_zero_denominator] = 0
    return np.mean(smape_value)
