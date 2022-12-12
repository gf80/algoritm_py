import math


def dfs(graph:dict, start, visited=None):

    #graph = {'0': set(['1', '2']),
    #'1': set(['0', '3', '4']),
    #'2': set(['0', '4']),
    #'3': set(['1']),
    #'4': set(['2', '3'])}

    if visited is None:
        visited = set()
    visited.add(start)

    print(f'из точки {start} {len(graph[start])} путей')

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

def draw(graph:dict):
    n = len(graph)
    print("  ",end='')  
    [print(str(i)+" ", end='') for i in range(n)]
    print()
    for i in graph:
        print(str(i)+"|", end="")
        for j in range(n):     
            if str(j) in graph[i]:
                print("1 ", end='')
            else:
                print("0 ", end='')
        print()
    print()
def dict_graph(n):
    graph = {}
    for i in range(n):
        graph[str(i)] = set()
    for i in range(n):
        for j in range(i+1,n):
            print(f'есть связь между вершиной {i} и {j}?')
            if input() == 'да':
                graph[str(i)].add(str(j))
                graph[str(j)].add(str(i))
            else:
                pass

    return graph


def list_graph(n):
    g = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i+1,n):
            print(f"Какое расстояние между {i} и {j}? ")
            g[i][j] = g[j][i] = int(input())

    return g

def deicstra(graph:list, start, end):
    N = len(graph)
    T = [math.inf] * N

    S = {start}
    T[start] = 0

    while start != -1:
        links = [i for i in range(len(graph[start])) if graph[start][i] > 0]
        for i in links:
            if i not in S:
                w = T[start] + graph[start][i]
                if w < T[i]:
                    T[i] = w

        amin = -1
        m = max(T)
        for i, t in enumerate(T):
            if t < m and i not in S:
                m = t
                amin = i
        start = amin
        if start > 0:
            S.add(start)

    return T[end]
