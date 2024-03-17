# Задание №3
import pandas as pd
# Функция для вычисления процентов к итогу, округлила до 3 знаков после запятой
def pr(series):
    total = series.sum()
    return series.apply(lambda x: round((x / total) * 100, 3))


# Чтение CSV-файла в DataFrame
df = pd.read_csv('regions.csv', encoding='windows-1251', sep=';', decimal=',', header=0)

# Выбор нужных столбцов
column_names = ['Население старше трудоспособного возраста на 2022 год',
                'Суммарный коэффициент рождаемости (число детей на 1 женщину) на 2022 год',
                'Ожидаемая продолжительность жизни при рождении на 2022 год']

# !!!! короче, тут такая проблема была, что он считывал не только чиселки, но и буквы из заголовков,
# поэтому мы превратим их в слово NaN (такое общепринятое сокращение Not-a-nuber), а потом сотрем все эти наны

# Проверка и преобразование столбцов в числовые типы данных
for column in column_names:
    df[column] = pd.to_numeric(df[column], errors='coerce')
    df.dropna(subset=[column], inplace=True)  # Удаление строк с NaN после преобразования

# Применение функции pr к каждому столбцу и сохранение результатов в списки
percentage_lists = [pr(df[column]).tolist() for column in column_names]
# Вывод результатов
for column, percentages in zip(column_names, percentage_lists):
    print(f"Проценты к итогу для переменной '{column}':")
    print(percentages)
    print()
# Создание списка со значениями в 100 %
hundred_percent_list = [100] * len(df)

# Проверка разницы между списком в 100 % и списками процентов к итогу
for column, percentages in zip(column_names, percentage_lists):
    difference = [abs(a - b) for a, b in zip(hundred_percent_list, percentages)]
    print(f"Разница между списком в 100 % и процентами к итогу для переменной '{column}':")
    print(difference)
    print()