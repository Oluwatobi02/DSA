def dfs(graph, root):
    stack = [root]
    while stack:
        cur = stack.pop()
        print(cur)
        for i in graph[cur]:
            stack.append(i)
    return 'done'

def recursivedfs(graph, source):
    print(source)
    for i in graph[source]:
        recursivedfs(graph, i)

def bfs(graph, root):
    queue = [root]
    while queue:
        cur = queue.pop(0)
        print(cur)
        for i in graph[cur]:
            queue.append(i)
    return 'done'

def has_path_dfs(graph, src, dst):
    if src == dst:
        return True
    for i in graph[src]:
        print(i)
        if has_path_dfs(graph, i, dst) == True: return True
    return False

def has_path_bfs(graph, src, dst):
    queue = [src]
    while queue:
        cur = queue.pop(0)
        print(cur)
        if cur == dst: return True
        for i in graph[cur]:
            queue.append(i)
    return False

graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd':['f'],
    'e': [],
    'f': []
}