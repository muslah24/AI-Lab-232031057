from collections import deque
def uninformed_search(graph,start,goal,strategy='bfs'):
    if strategy=='bfs':
        frontier=deque([[start]])
        explored=set()
        while frontier:
            path=frontier.popleft()
            node=path[-1]
            if node==goal:
                return path
            if node not in explored:
                explored.add(node)
                for n in graph.get(node,[]):
                    new_path=path+[n]
                    frontier.append(new_path)
    if strategy=='dfs':
        frontier=[[start]]
        explored=set()
        while frontier:
            path=frontier.pop()
            node=path[-1]
            if node==goal:
                return path
            if node not in explored:
                explored.add(node)
                for n in graph.get(node,[]):
                    new_path=path+[n]
                    frontier.append(new_path)
    return None