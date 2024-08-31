graph = {"A":["B","D"],"B":["C","E"],"C":["E"],"E":["D"],"D":["E"]}


visited = set()

def dfs(source,destination,visited):
    
    if(source in visited):
        return 0
    
    if(source == destination):
        return 1
    
    counter = 0
    visited.add(source)
    for x in graph[source]:
        counter  += dfs(x,destination,visited)
    visited.remove(source)
    return counter

def bfs(source,destination):
    visited = set()
    queue = [source]
    counter = 0
    while(queue.__len__()):
        node = queue.pop(0)

        if(node == destination):
            counter += 1

        for x in graph[node]:
            queue.append(x)
        

