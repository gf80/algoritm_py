import random



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
    m = len(arr[0])
    n = len(arr)
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

#Задание 3
def bin_search(a, x):
    l, r = 0, len(a) #Номера элементов (начало и конец)
    while r - l > 1: #Пока элементы справа больше чем середина и элементы слева больше чем элемент середины
        m = (r + l) // 2
        if a[m] <= x: #Если середина меньше искомого, то левая граница смещается
            l = m
        else: #Если середина больше искомого, то правая граница смещается
            r = m
    if l < 0 and a[r] == x:
        return f'Индекс элемента {r}'
    if a[l] == x:
        return f'Индекс элемента {l}'
    return "элемент в массиве не найден"

