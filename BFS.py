from collections import deque

def bfs(graph, start, goal):
    queue = deque([start])
    visited = {start: None}
  
    while queue:
        current = queue.popleft()
        
        if current == goal:
            path = []
            while current is not None:
                path.insert(0, current)
                current = visited[current]
            return path
        
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited[neighbor] = current
                queue.append(neighbor)
    
    return None
