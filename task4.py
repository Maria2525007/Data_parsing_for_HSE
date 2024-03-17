# Задание №4

import pandas as pd

# Функция для вычисления среднего
def mn(lst):
    return round(sum(lst) / len(lst), 3)

# Функция для вычисления медианы
def med(lst):
    n = len(lst)
    s = sorted(lst)
    return round((sum(s[n//2-1:n//2+1])/2.0, s[n//2])[n % 2], 3)

# Функция для вычисления моды (может не всегда дать корректный результат,
# если в списке несколько чисел с одинаковой частотой появления.
# В этом случае функция вернет только одно из таких чисел.)
def md(lst):
    return max(set(lst), key=lst.count)

# Функция для вычисления моды, в случае нескольких ответов выдаст "нет моды"
""" ура, я научилась делать многострочные комменты, а не сувать везде #
def md(lst):
    frequency = {}
    for item in lst:
        frequency[item] = frequency.get(item, 0) + 1
    max_freq = max(frequency.values())
    modes = [k for k, v in frequency.items() if v == max_freq]
    return modes[0] if modes else "Нет моды"
"""

# Функция для вычисления среднего квадратического отклонения
def sd(lst):
    mean = mn(lst)
    variance = sum((xi - mean) ** 2 for xi in lst) / len(lst)
    return round(variance ** 0.5, 3)

# Функция для вычисления размаха
def r(lst):
    return round(max(lst) - min(lst), 3)


# Чтение CSV-файла в DataFrame
df = pd.read_csv('regions.csv', encoding='windows-1251', sep=';', decimal=',', header=0)

# Выбор нужных столбцов
column_names = ['Население старше трудоспособного возраста на 2022 год',
                'Суммарный коэффициент рождаемости (число детей на 1 женщину) на 2022 год',
                'Ожидаемая продолжительность жизни при рождении на 2022 год']

# Запрос пользователя
functions = input("Введите названия функций через запятую (mn, med, md, sd, r): ").replace(' ', '').split(',')

# Создание списка для хранения результатов
results = []

# Вычисление характеристик для каждого столбца
for column in column_names:
    # Преобразование столбца в список, удаление NaN значений
    data = df[column].dropna().tolist()

    # Вычисление характеристик
    column_results = {}
    for func in functions:
        if func == 'mn':
            column_results['mn'] = mn(data)
        elif func == 'med':
            column_results['med'] = med(data)
        elif func == 'md':
            column_results['md'] = md(data)
        elif func == 'sd':
            column_results['sd'] = sd(data)
        elif func == 'r':
            column_results['r'] = r(data)

    # Добавление результатов для текущего столбца в общий список
    results.append({column: column_results})

# Вывод результатов более читабельным образом
for result in results:
    for column, values in result.items():
        print(f"{column}:")
        for func, value in values.items():
            print(f"{func}: {value}")
        print()