from curses.ascii import isdigit
import random 


def bubble_sort(n):  #сортировка пузырь
    for j in range(len(n)-1):
        for x in range(len(n)-1) :
            if n[x] > n[x+1]: #Если предыдущий больше последующего, то 
                n[x], n[x+1] = n[x+1],n[x] #меняем местами 
def vibor(n):
    smallest = 2**10
    for i in range(0, len(n) - 1):
        smallest = i
        for j in range(i + 1, len(n)):
            if n[j] < n[smallest]:
                smallest = j
        n[i], n[smallest] = n[smallest], n[i]
def vstavks(n):
    for i in range(1, len(n)):
        temp = n[i]
        j = i - 1
        while (j >= 0 and temp < n[j]):
            n[j + 1] = n[j]
            j = j - 1
        n[j + 1] = temp

def hoar(A): #Алгоритм Хоара
    if len(A) <= 1:
        return A
    else:
        q = random.choice(A)
        L = [elem for elem in A if elem < q]
        M = [q] * A.count(q)
        R = [elem for elem in A if elem > q] 
        return hoar(L) + M + hoar(R)

#Задание 1
def arr2sort(arr):
    n = len(arr[0])
    m = len(arr)
    rev_arr = [[0] * n for _ in range(m)] #Создаем новый массив, где столбцы меняем на строки

    for i in range(m):
        for j in range(n):
            rev_arr[i][j] = arr[j][i] #Создаем новый массив, где столбцы меняем на строки

    res_rev = []

    for i in range(len(rev_arr)):
        res_rev.append(hoar(rev_arr[i]))

    res_arr = [[0] * m for _ in range(n)] #Занова переворачиваем массив

    for i in range(n):
        for j in range(m):
            res_arr[i][j] = res_rev[j][i]

    return res_arr

#Задание 2
def merge_sort(alist, start, end):
    '''Sorts the list from indexes start to end - 1 inclusive.'''
    if end - start > 1:
        mid = (start + end)//2 #Середина массива
        merge_sort(alist, start, mid) #Сортируем одну часть массива
        merge_sort(alist, mid, end) #Сортируем вторую часть массива
 

        left = alist[start:mid]
        right = alist[mid:end]
        k = start
        i = 0
        j = 0
        while (start + i < mid and mid + j < end): #Сортируем 2 части массива
            if (left[i] <= right[j]):
                alist[k] = left[i]
                i = i + 1
            else:
                alist[k] = right[j]
                j = j + 1
            k = k + 1
        if start + i < mid: #Если элементы остались в левом массиве
            while k < end:
                alist[k] = left[i]
                i = i + 1
                k = k + 1
        else: #Если элементы остались в правом массиве
            while k < end:
                alist[k] = right[j]
                j = j + 1
                k = k + 1
#Заданиe 3
def bin_search(a, x):
    l, r = 0, len(a) #Номера элементов (начало и конец)
    while r - l > 1: #Пока элементы справа больше чем середина и элементы слева больше чем элемент середины
        m = (r + l) // 2
        if a[m] <= x: #Если середина меньше искомого, то левая граница смещается
            l = m
        else: #Если середина больше искомого, то правая граница смещается
            r = m
    if l < 0 and a[r] == x:
        return "Yes"
    if a[l] == x:
        return "Yes"
    return "элемент в массиве не найден"


def LIFO(sk:str):

    s = [] #Первый стек

    for i in sk:
        s.append(i)

    s_temp = [] #Временный стек

    while len(s) > 0:
        if len(s) > 0 and len(s_temp) == 0:
            s_temp.append(s.pop()) #Добавляем последний элемент в новый стек
            if s_temp[-1] == ')' and s[-1] == '(' or s_temp[-1] == ']' and s[-1] == '[' or s_temp[-1] == '}' and s[-1] == '{': #Если скобки закрываются
                s_temp.pop() #Удаляем элемент
                s.pop()
        else:
            if s_temp[-1] == ')' and s[-1] == '(' or s_temp[-1] == ']' and s[-1] == '[' or s_temp[-1] == '}' and s[-1] == '{': 
                s_temp.pop() #Удаляем элемент
                s.pop()
            else:
                s_temp.append(s.pop()) #Если нет пары полусле проверки, то удаляем из первого массива последний элемент и добавляем в новый массив

        if len(s) == 1:
            if len(s_temp) != 0: #Если остается полседний элемент
                if s_temp[-1] == ')' and s[-1] == '(' or s_temp[-1] == ']' and s[-1] == '[' or s_temp[-1] == '}' and s[-1] == '{':  #Если скобки закрываются
                    s_temp.pop()#Удаляем элемент
                    s.pop()
                else:
                    break #Если скобока не закрылась, то эта последовательность неверна
            else:
                break #Если нет скобок в другом массиве, то эта последовательность неверна
    if len(s) > 0:
        return "Неверная послдеовательность"
    else:
        return "Верная полседовательность"

def LIFO_calc(sk:str):
    s = [str(i) for i in sk] #Реальизуем стек

    s_sign = [] #Стек для знаков
    s_num = [] #Стек для цифр

    while len(s) > 0:
        if isdigit(str(s[-1])): # Если элемент - чилсло, то добавляем его в стек к числам
            s_num.append(s.pop())
        else:
            s_sign.append(s.pop())

    while len(s_num) != 0 or len(s_sign) != 0: #Заполняем массив обратно (сначала числа, потом знаки)
        if len(s_num) != 0:
            s.append(s_num.pop())
        elif len(s_sign) != 0:
            s.append(s_sign.pop())
    return " ".join(s)


