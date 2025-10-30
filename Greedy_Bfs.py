import heapq

def greedy_bfs(graph, start, goal, heuristic):
    frontier = [(heuristic[start], start)]
    parent = {start: None}
    
    while frontier:
        _, node = heapq.heappop(frontier)
        if node == goal:
            path = []
            while node is not None:
                path.insert(0, node)
                node = parent[node]
            return path
        
        for neighbor in graph.get(node, []):
            if neighbor not in parent:
                parent[neighbor] = node
                heapq.heappush(frontier, (heuristic[neighbor], neighbor))
    return None

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['E'],
    'D': ['E'],
    'E': []
}
heuristic = {'A': 7, 'B': 6, 'C': 2, 'D': 1, 'E': 0}

path = greedy_bfs(graph, 'A', 'E', heuristic)
print("Path found:", path)