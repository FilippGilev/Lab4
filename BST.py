import random
import time
from graphviz import Digraph
import matplotlib.pyplot as plt

# Класс для создания узла бинарного дерева
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Класс для создания бинарного дерева
class BinarySearchTree:
    def __init__(self):
        self.root = None
    # Метод для добавления узла в дерево
    def add(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._add(key, self.root)
    # Вспомогательный метод для рекурсивного добавления узла в дерево
    def _add(self, key, node):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._add(key, node.left)
        elif key > node.val:
            if node.right is None:
                node.right = Node(key)
            else:
                self._add(key, node.right)
    # Метод для поиска узла в дереве
    def search(self, key):
        return self._search(key, self.root)
    # Вспомогательный метод для рекурсивного поиска узла в дереве
    def _search(self, key, node):
        if node is None or node.val == key:
            return node
        elif key < node.val:
            return self._search(key, node.left)
        else:
            return self._search(key, node.right)
    # Метод для удаления узла из дерева
    def delete(self, key):
        self.root = self._delete(key, self.root)
    # Вспомогательный метод для рекурсивного удаления узла из дерева
    def _delete(self, key, node):
        if node is None:
            return node
        elif key < node.val:
            node.left = self._delete(key, node.left)
        elif key > node.val:
            node.right = self._delete(key, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_node = self._find_min(node.right)
                node.val = min_node.val
                node.right = self._delete(min_node.val, node.right)
        return node

    # Метод для поиска минимального узла в дереве
    def find_min(self):
        return self._find_min(self.root)

    # Вспомогательный метод для рекурсивного поиска минимального узла в дереве
    def _find_min(self, node):
        if node.left is None:
            return node
        else:
            return self._find_min(node.left)

    # Метод для визуализации бинарного дерева поиска
    def visualize(self):
        dot = Digraph()
        if self.root:
            self._visualize(self.root, dot)
        dot.render('binary_tree', format='png', cleanup=True)
        img = plt.imread('binary_tree.png')
        plt.imshow(img)
        plt.axis('off')
        plt.show()

    # Вспомогательный метод для рекурсивной визуализации бинарного дерева
    def _visualize(self, node, dot):
        if node.left:
            dot.node(str(node.left.val))
            dot.edge(str(node.val), str(node.left.val))
            self._visualize(node.left, dot)
        if node.right:
            dot.node(str(node.right.val))
            dot.edge(str(node.val), str(node.right.val))
            self._visualize(node.right, dot)

# Создание экземпляра класса BinarySearchTree
bst = BinarySearchTree()

# Генерация случайных чисел для построения дерева
n = int(input("Введите количество элементов: "))
min_limit = int(input("Введите минимальное значение: "))
max_limit = int(input("Введите максимальное значение: "))

massiv = [0 for i in range(n)]
for i in range(n):
   massiv[i] = random.randint(min_limit, max_limit)
print(massiv)

# Добавление элементов в дерево
for number in massiv:
    bst.add(number)

# Визуализация дерева
bst.visualize()

print("\n1. Найти число\n2. Добавить число\n3. Удалить число\n4. Завершить программу")
while True:
   action = int(input("Выберите действие: "))
   match action:
      case 1:
         num = int(input("Введите число, которое нужно найти: "))
         start_time_bst = time.perf_counter()
         result_search_bst = bst.search(num)
         finish_time_bst = time.perf_counter() - start_time_bst
         if result_search_bst is not None:
             print('Элемент', num, 'найден в дереве')
         else:
             print('Элемент', num, 'не найден в дереве')
         print("\nВремя выполнения")
         print("--- {0} mcs ---".format(round(finish_time_bst * 1000000)))
      case 2:
          add_num = int(input("\nВведите число, которое хотите добавить: "))
          result_add_bst = bst.add(add_num)
          bst.visualize()
      case 3:
          delete_num = int(input("\nВведите число, которое хотите удалить: "))
          result_delete_bst = bst.delete(delete_num)
          bst.visualize()
          if result_delete_bst is not None:
              print('Элемент', delete_num, 'удален')
          else:
              print('Элемент', delete_num, 'не найден в дереве')
      case 4:
         print("Программа завершена")
         break