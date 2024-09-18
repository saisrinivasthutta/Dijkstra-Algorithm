import heapq

def dijkstra(graph, src):
    length = len(graph)
    type_ = type(graph)
    if type_ == list:
        nodes = [i for i in range(length)]
    elif type_ == dict:
        nodes = list(graph.keys())
    else:
        raise TypeError("Graph must be a list or a dictionary")

    visited = set()
    path = {src: {src: []}}
    distance_graph = {src: 0}
    queue = [(0, src)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if neighbor not in distance_graph or distance < distance_graph[neighbor]:
                distance_graph[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
                path[src][neighbor] = path[src][current_node] + [neighbor]

    return distance_graph, path

if __name__ == '__main__':
    graph_dict = {
        "s1": {"s1": 0, "s2": 2, "s10": 1, "s12": 4, "s5": 3},
        "s2": {"s1": 1, "s2": 0, "s10": 4, "s12": 2, "s5": 2},
        "s10": {"s1": 2, "s2": 1, "s10": 0, "s12": 1, "s5": 4},
        "s12": {"s1": 3, "s2": 5, "s10": 2, "s12": 0, "s5": 1},
        "s5": {"s1": 3, "s2": 5, "s10": 2, "s12": 4, "s5": 0},
    }

    distance, path = dijkstra(graph_dict, 's1')
    print(distance, '\n', path)