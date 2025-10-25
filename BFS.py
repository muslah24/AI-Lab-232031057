from collections import deque
def bfs(graph,start,goal):
    frontier=deque([start])
    parent={start:None}
    while frontier:
        node=frontier.popleft()
        if node==goal:
            path=[]
            while node is not None:
                path.append(node)
                node=parent[node]
            return path[::-1]
        for n in graph.get(node,[]):
            if n not in parent:
                parent[n]=node
                frontier.append(n)
    return None