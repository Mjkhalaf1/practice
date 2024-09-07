def BFS(graph , node):
    visited = []
    queue = []
    queue.append(node)
    while queue:
        current = queue[0]
        for i in graph[current]:
            if i not in visited:
                queue.append(i)
        if current not in visited:
            print(current ,end=" ")
            visited.append(queue.pop(0))
        else:
            queue.pop(0)
            
def DFS(graph , node):
    visited = []
    stack = []
    stack.append(node)
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)
            print(current, end=" ")
        for i in reversed(graph[current]):
            if i not in visited:
                stack.append(i)

graph2 = {
    '47': ['21', '76'],
    '21': ['18' , '27'],
    '76': ['27' , '52' , '82'],
    '18': [],
    '27': ['1'],
    '52': [],
    '82': [],
    '1' : []
}
BFS(graph2,'47')
print("----------------------------------")

graph3 = {
    'A': ['B', 'G'],
    'B': ['C', 'D', 'E'],
    'C': [],
    'D': [],
    'E': ['F'],
    'F': [],
    'G': ['H'],
    'H': ['I'],
    'I': []
}
DFS(graph3,'A')
