import random
import time

n = int(input("Введите количество элементов: "))
min_limit = int(input("Введите минимальное значение: "))
max_limit = int(input("Введите максимальное значение: "))

print("\nСгенерированный массив:")
massiv = [0 for i in range(n)]
for i in range(n):
   massiv[i] = random.randint(min_limit, max_limit)
print(massiv)

simple_hash_table = {}
random_hash_table = {}
chains_hash_table = {}

#Вычисление индекса с помощью хэш-функции
def hash_function(value, table_size):
   return value % table_size

#Создание таблицы методом простого рехеширования
def simple_hash(hash_table, table_size):
    hash_table = {}
    for i in range(n):
        key = hash_function(massiv[i], table_size)
        while key in hash_table:
            # Если индекс уже занят ищем пустую ячейку
            key = (key + 1) % table_size
        hash_table[key] = massiv[i]
    return hash_table

#Поиск значения в хэш-таблице методом простого рехеширования
def simple_search(value, hash_table, table_size):
    key = hash_function(value, table_size)
    while hash_table.get(key) != value:
        key = (key + 1) % table_size
        if key == hash_function(value, table_size):
            return -1
    return key

#Добавление значения в хэш-таблицу методом простого рехеширования
def simple_add(value, hash_table, table_size):
    key = hash_function(value, table_size)
    while key in hash_table:
        key = (key + 1) % table_size
    hash_table[key] = value

    # При переполнении таблицы на 70% и более увеличиваем размер таблицы вдвое
    if len(hash_table) >= table_size * 0.7:
        hash_table = simple_resize(hash_table, table_size * 2)
    return hash_table

#Удаление значения из хэш-таблицы методом простого рехеширования
def simple_delete(value, hash_table, table_size):
    key = hash_function(value, table_size)
    while hash_table.get(key) != value:
        key = (key + 1) % table_size
        # Если мы вернулись к индексу с которого начали значит числа нет
        if key == hash_function(value, table_size):
            return -1
    del hash_table[key]
    return hash_table

#Изменяем размер таблицы
def simple_resize(hash_table, new_size):
    new_hash_table = {}
    for key, value in hash_table.items():
        new_hash_table = simple_add(value, new_hash_table, new_size)
    return new_hash_table

#Создание таблицы псевдослучайными числами
def random_hash(hash_table, table_size):
    hash_table = {}
    for i in range(n):
        key = hash_function(massiv[i], table_size)
        while key in hash_table: # Если индекс уже занят
            key = random.randint(0, n - 1) # генерируем новый индекс пока не найдем пустую ячейку
        hash_table[key] = massiv[i]
    return hash_table

#Поиск числа с помощью псевдослучайных чисел
def random_search(value, hash_table, table_size):
    key = hash_function(value, table_size)
    checked_index = set()
    while hash_table.get(key) != value:
        checked_index.add(key)
        while True:
            new_key = random.randint(0, n - 1)
            if new_key not in checked_index:
                key = new_key
                break

        if len(checked_index) == n - 1:
            if hash_table.get(key) != value:
                return -1
    return key

#Добавление числа с помощью псевдослучайных чисел
def random_add(value, hash_table, table_size) :
    key = hash_function(value, table_size)
    while key in hash_table:
        key = random.randint(0, n - 1)
    hash_table[key] = value

    if len(hash_table) >= table_size * 0.7:  # Загруженность более 70%
        hash_table = random_resize(hash_table, table_size * 2)
    return hash_table

#Удаление числа с помощью псевдослучайных чисел
def random_delete(value, hash_table, table_size) :
    key = hash_function(value, table_size)
    checked_index = set()
    while hash_table.get(key) != value:
        checked_index.add(key)
        while True:
            new_key = random.randint(0, n - 1)
            if new_key not in checked_index:
                key = new_key
                break
        if len(checked_index) == n - 1:
            if hash_table[key] != value:
                return -1

    del hash_table[key]
    return hash_table

#Изменение размера таблицы
def random_resize(hash_table, new_size):
    new_hash_table = {}
    for key, value in hash_table.items():
        new_hash_table = random_add(value, new_hash_table, new_size)
    return new_hash_table

#Создание хэш-таблицы методом цепочек
def chains_hash(hash_table, table_size):
    hash_table = {}
    for i in range(n):
        key = hash_function(massiv[i], table_size)
        if key in hash_table:
            hash_table[key].append(massiv[i])
        hash_table[key] = [massiv[i]]
    return hash_table

#Поиск числа в хэш-таблице методом цепочек
def chains_search(value, hash_table, table_size):
    key = hash_function(value, table_size)
    if key in hash_table:
        if value in hash_table[key]:
            return key
    return -1

#Добавление числа в хэш-таблицу методом цепочек
def chains_add(value, hash_table, table_size):
    key = hash_function(value, table_size)
    if key not in hash_table:
        hash_table[key] = [value]
    else:
        hash_table[key].append(value)

    if len(hash_table) >= table_size * 0.7:  # Загруженность более 70%
        hash_table = chains_resize(hash_table, table_size * 2)

    return hash_table

#Удаление числа из хэш-таблицы методом цепочек
def chains_delete(value, hash_table, table_size):
    key = hash_function(value, table_size)
    if key in hash_table:
        if value in hash_table[key]:
            hash_table[key].remove(value)
            if not hash_table[key]:  # Если цепочка стала пустой
                del hash_table[key]
        else:
            return -1
    return hash_table

#Изменение размера таблицы
def chains_resize(hash_table, new_size):
    new_hash_table = {}
    for key, values in hash_table.items():
        for value in values:
            new_key = hash_function(value, new_size)
            if new_key not in new_hash_table:
                new_hash_table[new_key] = [value]
            else:
                new_hash_table[new_key].append(value)
    return new_hash_table

table_size = n * 2

num = int(input("Введите число, которое нужно найти: "))

#Создание хэш таблицы (простое рехеширование)
simple_hash_table = simple_hash(simple_hash_table, table_size)
print("\nПростое рехеширование:", simple_hash_table)
start_time_simple = time.perf_counter()
#Поиск числа в хэш-таблице
result_simple = simple_search(num, simple_hash_table, table_size)
finish_time_simple = time.perf_counter() - start_time_simple
if result_simple == -1:
    print(f"Число {num} не найдено")
else:
    print(f"Число {num} найдено на позиции {result_simple}")
print("\nВремя выполнения")
print("--- {0} mcs ---".format(round(finish_time_simple * 1000000)))

#Добавление числа в хэш-таблицу
add_num_simple = int(input("\nВведите число, которое нужно добавить: "))
simple_result_add = simple_add(add_num_simple, simple_hash_table, table_size)
print("\nЧисло добавлено:", simple_result_add)

#Удаление числа из хэш-таблицы
delete_num_simple = int(input("\nВведите число, которое нужно удалить: "))
simple_result_delete = simple_delete(delete_num_simple, simple_hash_table, table_size)
if simple_result_delete == -1:
    print("\nЧисло не найдено:")
else:
    print("\nЧисло удалено:", simple_result_delete)

#Создание хэш таблицы (рехеширование с псевдослучайными числами)
random_hash_table = random_hash(random_hash_table, table_size)
print("\nРехеширование псевдослучайными числами:", random_hash_table)
start_time_random = time.perf_counter()
#Поиск числа в хэш-таблице
result_random = random_search(num, random_hash_table, table_size)
finish_time_random = time.perf_counter() - start_time_random
if result_random == -1:
    print(f"Число {num} не найдено")
else:
    print(f"Число {num} найдено на позиции {result_random}")
print("\nВремя выполнения")
print("--- {0} mcs ---".format(round(finish_time_random * 1000000)))

#Добавление числа в хэш-таблицу
add_num_random = int(input("\nВведите число, которое нужно добавить: "))
random_result_add = random_add(add_num_random, random_hash_table, table_size)
print("\nЧисло добавлено:", random_result_add)

#Удаление числа из хэш-таблицы
delete_num_random = int(input("\nВведите число, которое нужно удалить: "))
random_result_delete = random_delete(delete_num_random, random_hash_table, table_size)
if random_result_delete == -1:
    print("\nЧисло не найдено:")
else:
    print("\nЧисло удалено:", random_result_delete)

#Создание хэш таблицы (Метод цепочек)
chains_hash_table = chains_hash(chains_hash_table, table_size)
print("\nМетод цепочек:", chains_hash_table)
start_time_chains = time.perf_counter()
#Поиск числа в хэш-таблице
result_chains = chains_search(num, chains_hash_table, table_size)
finish_time_chains = time.perf_counter() - start_time_chains
if result_chains == -1:
    print(f"Число {num} не найдено")
else:
    print(f"Число {num} найдено на позиции {result_chains}")
print("\nВремя выполнения")
print("--- {0} mcs ---".format(round(finish_time_chains * 1000000)))

#Добавление числа в хэш-таблицу
add_num_chains = int(input("\nВведите число, которое нужно добавить: "))
chains_result_add = chains_add(add_num_chains, chains_hash_table, table_size)
print("\nЧисло добавлено:", chains_result_add)

#Удалениие числа из хэш-таблицы
delete_num_chains = int(input("\nВведите число, которое нужно удалить: "))
chains_result_delete = chains_delete(delete_num_chains, chains_hash_table, table_size)
if random_result_delete == -1:
    print("\nЧисло не найдено:")
else:
    print("\nЧисло удалено:", chains_result_delete)


