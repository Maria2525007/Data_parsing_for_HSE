# Задание №1
# Файл csv уже подготовлен и находится в этом же проекте (слева, если ты работаешь в pycharm)
# Файл называется regions.csv

import pandas as pd
from tabulate import tabulate


# Задание №2
# Функция для создания словаря из CSV файла
def create_regions_dict():
    # Чтение CSV файла с помощью pandas с указанием кодировки, разделителя и отметка о том,
    # что заголовки в файле не читаем, а назначим свои (наколько я поняла, изначально заголовки - это А, В, С и тд.)
    df = pd.read_csv('regions.csv', encoding='windows-1251', sep=';', header=None)
    # назначили свои заголовки
    df.columns = ['Наименование федерального округа', 'Наименования субъекта РФ',
                  'Население старше трудоспособного возраста на 2022 год',
                  'Суммарный коэффициент рождаемости (число детей на 1 женщину) на 2022 год',
                  'Ожидаемая продолжительность жизни при рождении на 2022 год']

    # Создание словаря по ключам Федеральный округ и вложенный словарь по ключам наименование субъекта РФ
    regions_dict = {}

    for index, row in df.iterrows():
        federal_district = row['Наименование федерального округа']
        region_name = row['Наименования субъекта РФ']
        population = row['Население старше трудоспособного возраста на 2022 год']
        birth_rate = row['Суммарный коэффициент рождаемости (число детей на 1 женщину) на 2022 год']
        life_expectancy = row['Ожидаемая продолжительность жизни при рождении на 2022 год']
        # Проверка наличия федерального округа в словаре и создание, если не существует
        if federal_district not in regions_dict:
            regions_dict[federal_district] = {}
        # Добавление данных о регионе в словарь
        regions_dict[federal_district][region_name] = {
            'Население старше трудоспособного возраста на 2022 год': population,
            'Суммарный коэффициент рождаемости (число детей на 1 женщину) на 2022 год': birth_rate,
            'Ожидаемая продолжительность жизни при рождении на 2022 год': life_expectancy
        }

    return regions_dict


# Создание словаря из файла (применяем созданную функцию)
regions_dict = create_regions_dict()


# Функция для вывода значений по ключам
# def get_region_data(regions_dict, federal_district, region_name):
# return regions_dict[federal_district][region_name]

# Функция для вывода значений по ключам в виде таблицы
def get_region_data(regions_dict, federal_district, region_name):
    data = regions_dict[federal_district][region_name]
    # Преобразование словаря в список кортежей для tabulate
    table_data = [[k, v] for k, v in data.items()]
    # Добавление заголовков столбцов
    headers = [federal_district + ', ' + region_name, 'Значение']
    # Форматирование в виде таблицы
    table = tabulate(table_data, headers, tablefmt="grid")
    return table


# Функция для вывода значений для одного федерального округа с помощью ключей
# def get_federal_district_data(regions_dict, federal_district):
# return regions_dict.get(federal_district, {})

# Функция для вывода значений для одного федерального округа с помощью ключей в виде таблицы
def get_federal_district_data(regions_dict, federal_district):
    federal_data = regions_dict.get(federal_district, {})
    # Преобразование словаря в список кортежей для tabulate
    table_data = []
    for region_name, region_data in federal_data.items():
        # Добавление федерального округа и региона в каждый ряд
        row = [region_name]
        # Добавление значений параметров в ряд
        row.extend(region_data.values())
        table_data.append(row)
    # Добавление заголовков столбцов
    headers = ['Регион', 'Население старше трудоспособного \nвозраста на 2022 год',
               'Суммарный коэффициент рождаемости \n(число детей на 1 женщину) на 2022 год',
               'Ожидаемая продолжительность \nжизни при рождении на 2022 год']
    # Форматирование в виде таблицы
    table = tabulate(table_data, headers, tablefmt="grid")
    # Добавление строки федерального округа над заголовками
    table = f"Федеральный округ: {federal_district}\n{table}"
    return table


# Функция для вывода значений для одного федерального округа с помощью цикла
# def get_federal_district_data_loop(regions_dict, federal_district):
#    result = {}
#   for region_name, data in regions_dict.get(federal_district, {}).items():
#      result[region_name] = data
#     print(region_name, result[region_name])

# Функция для вывода значений для одного федерального округа с помощью цикла в виде таблицы
def get_federal_district_data_loop(regions_dict, federal_district):
    federal_data = regions_dict.get(federal_district, {})
    # Преобразование словаря в список кортежей для tabulate
    table_data = []
    for region_name, region_data in federal_data.items():
        # Добавление федерального округа и региона в каждый ряд
        row = [region_name]
        # Добавление значений параметров в ряд
        row.extend(region_data.values())
        table_data.append(row)
    # Добавление заголовков столбцов
    headers = ['Регион', 'Население старше трудоспособного \nвозраста на 2022 год',
               'Суммарный коэффициент рождаемости \n(число детей на 1 женщину) на 2022 год',
               'Ожидаемая продолжительность \nжизни при рождении на 2022 год']
    # Форматирование в виде таблицы
    table = tabulate(table_data, headers, tablefmt="grid")
    # Добавление строки федерального округа над заголовками
    table = f"Федеральный округ: {federal_district}\n{table}"
    return table


# Пример использования функций
print(get_region_data(regions_dict, 'Уральский федеральный округ', 'Тюменская область (без АО)'))
print()
print(get_federal_district_data(regions_dict, 'Северо-Западный федеральный округ'))
print()
print(get_federal_district_data_loop(regions_dict, 'Дальневосточный федеральный округ'))
