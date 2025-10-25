def dls(graph,start,goal,limit):
    def recurse(node,depth,visited):
        if node==goal:
            return [node]
        if depth==0:
            return None
        for n in graph.get(node,[]):
            if (node,n,depth) not in visited:
                visited.add((node,n,depth))
                res=recurse(n,depth-1,visited)
                if res:
                    return [node]+res
        return None
    return recurse(start,limit,set())