def dfs(graph,start,goal):
    stack=[start]
    parent={start:None}
    visited=set()
    while stack:
        node=stack.pop()
        if node==goal:
            path=[]
            while node is not None:
                path.append(node)
                node=parent[node]
            return path[::-1]
        if node not in visited:
            visited.add(node)
            for n in graph.get(node,[]):
                if n not in parent:
                    parent[n]=node
                stack.append(n)
    return None