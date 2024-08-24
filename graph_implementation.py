from collections import defaultdict
# n = int(input())

# graph = defaultdict(list)

# for _ in range(n):
#     g = list(input().split())
#     curr_node = int(g[0])
#     for i in range(1, len(g)):
#         neighbor = tuple(map(int, g[i].split(',')))
#         graph[curr_node].append(neighbor)

# print(graph)

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

print(graph)