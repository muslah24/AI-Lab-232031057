from DLS import dls


def ids(graph,start,goal,max_depth=50):
    for depth in range(max_depth+1):
        path=dls(graph,start,goal,depth)
        if path:
            return path
    return None