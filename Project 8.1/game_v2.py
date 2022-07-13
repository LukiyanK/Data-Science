"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0   
    predict_number = 100  # предполагаемое число
    min_predict_number=1 # хранение предыдущего значения меньше искомого
    max_predict_number=100 # хранение предыдущего начения больше искомого
    while True:
        count += 1
        # сужаем диапазон возможных значений
        if predict_number > number:
            max_predict_number = predict_number
            predict_number = np.random.randint(min_predict_number, predict_number+1)
        elif predict_number < number:
            min_predict_number = predict_number
            predict_number = np.random.randint(predict_number, max_predict_number+1)
        # когда найдено число происходит выход из цикла while
        else:
            break
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
