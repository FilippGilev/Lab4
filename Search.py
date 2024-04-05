import random
import time

n = int(input("Введите количество элементов: "))
min_limit = int(input("Введите минимальное значение: "))
max_limit = int(input("Введите максимальное значение: "))

print("\nСгенерированный массив:")
massiv = [0 for i in range(n)]
for i in range(n):
   massiv[i] = random.randint(min_limit, max_limit)
massiv = sorted(massiv)
print(massiv)

#Бинарный поиск
def Bin_search(massiv, num):
   min_index = 0
   max_index = len(massiv) - 1
   #Начинаем поиск с середины массива
   index = (min_index + max_index) // 2
   while min_index <= max_index:
      # Если число равно искомому числу выводим индекс
      if massiv[index] == num:
         return index
      # Если меньше искомого числа
      elif massiv[index] < num:
         # Отбрасываем все левее этого числа
         min_index = index + 1
         index = (min_index + max_index) // 2
      # Если больше искомого числа
      elif massiv[index] > num:
         # Отбрасываем все правее этого числа
         max_index = index - 1
         index = (min_index + max_index) // 2
   return -1

#Фибоначчиев поиск
def Fibonacci_search(massiv, num):
   fib_1 = 0
   fib_2 = 1
   fib_3 = fib_1 + fib_2
   #Находим минимальное число Фибоначчи большее длины массива
   while fib_3 < len(massiv):
      fib_1 = fib_2
      fib_2 = fib_3
      fib_3 = fib_1 + fib_2

   offset = -1
   while fib_3 > 1:
      # Находим индекс с использованием чисел Фибоначчи
      i = min(offset + fib_1, len(massiv) - 1)
      # Если элемент на этой позиции меньше искомого числа,
      # продвигаемся вправо, уменьшая числа Фибоначчи
      if massiv[i] < num:
         fib_3 = fib_2
         fib_2 = fib_1
         fib_1 = fib_3 - fib_2
         offset = i
      # Если элемент на позиции больше искомого числа,
      # продвигаемся влево, изменяя числа Фибоначчи
      elif massiv[i] > num:
         fib_3 = fib_1
         fib_2 = fib_2 - fib_1
         fib_1 = fib_3 - fib_2
      else:
         # Если число найдено выводим его позицию
         return i
   # Если число не найдено и осталось только одно число Фибоначчи,
   # проверяем следующий элемент за последним индексом,
   if fib_2 == 1 and massiv[offset + 1] == num:
      return offset + 1
   # Если число не найдено
   return -1

#Интеполяционный поиск
def Interpolation_search(massiv, num):
   min_index = 0
   max_index = len(massiv) - 1
   #Начинаем поиск с числа находящегося на позиции вычисляемой по формуле
   index = min_index + int((max_index - min_index) * (num - massiv[min_index]) / (massiv[max_index] - massiv[min_index]))
   while min_index <= max_index:
      # Если число равно искомому числу выводим индекс
      if massiv[index] == num:
         return index
      # Если меньше искомого числа
      elif massiv[index] < num:
         min_index = index + 1 # Отбрасываем все левее этого числа
         index = min_index + int((max_index - min_index) * (num - massiv[min_index]) / (massiv[max_index] - massiv[min_index]))
      # Если больше искомого числа
      elif massiv[index] > num:
         max_index = index - 1 # Отбрасываем все правее этого числа
         index = min_index + int((max_index - min_index) * (num - massiv[min_index]) / (massiv[max_index] - massiv[min_index]))
   return -1

print("\n1. Найти число\n2. Добавить число\n3. Удалить число\n4. Завершить программу")
while True:
   action = int(input("Выберите действие: "))
   match action:
      case 1:
         num = int(input("Введите число, которое нужно найти: "))
         start_time_index = time.perf_counter()
         result_index = massiv.index(num)
         finish_time_index = time.perf_counter() - start_time_index
         print("\nВстроенная функция поиска:")
         if result_index == -1:
             print(f"Число {num} не найдено")
         else:
             print(f"Число {num} найдено на позиции {result_index}")
         print("\nВремя выполнения")
         print("--- {0} mcs ---".format(round(finish_time_index * 1000000)))

         start_time_bin = time.perf_counter()
         result_bin = Bin_search(massiv, num)
         finish_time_bin = time.perf_counter() - start_time_bin
         print("\nБинарный поиск:")
         if result_bin == -1:
            print(f"Число {num} не найдено")
         else:
            print(f"Число {num} найдено на позиции {result_bin}")
         print("\nВремя выполнения")
         print("--- {0} mcs ---".format(round(finish_time_bin * 1000000)))

         start_time_fib = time.perf_counter()
         result_fib = Fibonacci_search(massiv, num)
         finish_time_fib = time.perf_counter() - start_time_fib
         print("\nФибоначчиев поиск:")
         if result_fib == -1:
            print(f"Число {num} не найдено")
         else:
            print(f"Число {num} найдено на позиции {result_fib}")
         print("\nВремя выполнения")
         print("--- {0} mcs ---".format(round(finish_time_fib * 1000000)))

         start_time_interp = time.perf_counter()
         result_interp = Interpolation_search(massiv, num)
         finish_time_interp = time.perf_counter() - start_time_interp
         print("\nИнтерполяционный поиск:")
         if result_interp == -1:
            print(f"Число {num} не найдено")
         else:
            print(f"Число {num} найдено на позиции {result_interp}")
         print("\nВремя выполнения")
         print("--- {0} mcs ---\n".format(round(finish_time_interp * 1000000)))
      case 2:
         add_num = int(input("Введите число, которое нужно добавить: "))
         massiv.append(add_num)
         massiv = sorted(massiv)
         print(massiv)
      case 3:
         del_num = int(input("Введите число, которое нужно удалить: "))
         if del_num in massiv:
            massiv.remove(del_num)
            print(massiv)
         else:
            print("Число не найдено")
            print(massiv)
      case 4:
         print("Программа завершена")
         break

