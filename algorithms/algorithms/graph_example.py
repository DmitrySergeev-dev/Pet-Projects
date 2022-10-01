infinity = float("inf")  # бесконечность
graph = {}
graph["start"] = {}
graph["start"]["A"] = 6
graph["A"] = {}
graph["A"]["finish"] = 1
graph["start"]["B"] = 2
graph["B"] = {}
graph["B"]["A"] = 3
graph["B"]["finish"] = 5
graph["finish"] = {}

costs = {}  # хеш таблица стоимостей
costs["A"] = 6
costs["B"] = 2
costs["finish"] = infinity

parents = {}  # хеш таблица родителей
parents["A"] = "start"
parents["B"] = "start"
parents["finish"] = None

processed = []  # для хранения пройденных узлов


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for neighbor in neighbors.keys():
        new_cost = cost + neighbors[neighbor]
        if costs[neighbor] > new_cost:
            costs[neighbor] = new_cost
            parents[neighbor] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
print(costs, parents, graph, sep="\n")
