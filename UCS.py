import heapq
def ucs(graph,start,goal):
    frontier=[]
    heapq.heappush(frontier,(0,start))
    parent={start:None}
    cost={start:0}
    while frontier:
        c,node=heapq.heappop(frontier)
        if node==goal:
            path=[]
            while node is not None:
                path.append(node)
                node=parent[node]
            return path[::-1]
        if c>cost.get(node, float('inf')):
            continue
        for n, w in graph.get(node,[]):
            new_cost=c+w
            if new_cost<cost.get(n,float('inf')):
                cost[n]=new_cost
                parent[n]=node
                heapq.heappush(frontier,(new_cost,n))
    return None