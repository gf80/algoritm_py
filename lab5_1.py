import random
from lab1 import *
from lab2 import *
from lab3 import *
from lab4 import *
from lab5 import *

n = input("Введите номер лабораторной: (1,2,3,4,5) ")
if n in '12345':
    if n == '1':
        q = input("Введите метод сортировки:\n(1. Пузырьком)\n2. Выборкой\n3. Вставками)\n")
        if q in '123':
            try:
                arr = [int(i) for i in input("Введите числа через пробел:\n").split()]
            except:
                print("Неправлиньно введен массив!")
            try:
                if q == "1":
                    print(bubble_sort(arr))
                elif q == "2":
                    print(vibor(arr))
                elif q == "3":
                    print(vstavks(arr))

            except Exception as e:
                print(e)
        else:
            print("Неверно выбранный метод!")
    elif n == "2":
        q = input("Введите метод сортировки или поиска:\n(1. Столбцы двумерных массивов\n2. Слиянием\n3. Бинарный поиск)\n")
        if q in '123':
            try:
                if q == "1":
                    try:
                        n,m = map(int, input("Введите количество стобцов, затем количество строк: ").split())
                    except Exception:
                        if ValueError:
                            print("Неверно введены данные!")
                    arr = []
                    for i in range(m):
                        a = []
                        for j in range(n):
                            a.append(random.randint(0,100))
                        arr.append(a)
                    print(arr2sort(arr))
                elif q == "2":
                    try:
                        arr = [int(i) for i in input("Введите числа через пробел:\n").split()]
                    except:
                        print("Неправлиньно введен массив!")

                    merge_sort(arr,0,len(arr))
                    print(arr)
                else:
                    try:
                        arr = [int(i) for i in input("Введите числа через пробел:\n").split()]
                    except:
                        print("Неправлиньно введен массив!")
                    try:
                        n = input("Какое число найти: ")
                    except:
                        print("Можно искть только числа!")
                    print(bin_search(arr,int(n)))
            except Exception as e:
                print(e)
                
        else:
            print("Неверно выбранный метод!")
        
    elif n == "3":
        q = input("Введите метод сортировки или поиска:\n(1. Стек\n2. Слиянием\n2. Польсктй калькулятор)\n")
        if q in "12":
            try:
                if q == "1":
                    s = input("Введите полседовательность скобок: ")
                    print(LIFO(s))
                else:
                    s = input("Введите мат. пример: ")
                    print(LIFO_calc(s))
            except Exception as e:
                print(e)
        else:
            print("Неверно выбранный метод!")
    elif n == "4":
        q = input("Введите метод сортировки или поиска:\n(1. Поиск в глубину\n2. Нарисовать граф\n3. Алгоритм Дейкстры)\n")
        if q in '123':
            try:
                if q == '1':
                    n = int(input("Введите количество вершин: "))
                    graph = dict_graph(n)
                    dfs(graph)
                elif q == "2":
                    n = int(input("Введите количество вершин: "))
                    graph = dict_graph(n)
                    draw(graph)
                else:
                    n = int(input("Введите количество вершин: "))
                    graph = list_graph(n)
                    deicstra(graph)
            except Exception as e:
                print(e)
        else:
            print("Неверно выбранный метод!")
    else:
        q = input("Введите метод сортировки:\n(1. Пирамидная 1)\n2. Пирамидная 2\n")
        if q in '12':
            try:
                arr = [int(i) for i in input("Введите числа через пробел:\n").split()]
            except:
                print("Неправлиньно введен массив!")
            try:
                if q == "1":
                    heapSort(arr)
                    print(arr)
                elif q == "2":
                    print(heapsort(arr))
            except Exception as e:
                print(e)
        else:
            print("Неверно выбранный метод!")
else:
    print("Такой работы нет!")