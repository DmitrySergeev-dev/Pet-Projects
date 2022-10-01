infinity = float("inf")  # бесконечность
graph = {}
graph["start"] = {}
graph["start"]["A"] = 5
graph["start"]["B"] = 2

graph["A"] = {}
graph["A"]["C"] = 4
graph["A"]["D"] = 2

graph["B"] = {}
graph["B"]["A"] = 8
graph["B"]["D"] = 7

graph["C"] = {}
graph["C"]["D"] = 6
graph["C"]["finish"] = 3

graph["D"] = {}
graph["D"]["finish"] = 1

graph["finish"] = {}

costs = {}  # хеш таблица стоимостей
costs["A"] = 5
costs["B"] = 2
costs["C"] = infinity
costs["D"] = infinity
costs["finish"] = infinity

parents = {}  # хеш таблица родителей
parents["A"] = "start"
parents["B"] = "start"
parents["C"] = "start"
parents["D"] = "start"
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
