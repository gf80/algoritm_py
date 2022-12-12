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



