# Problem:  Network Topology - https://codeforces.com/problemset/problem/292/B

from collections import defaultdict

n, e = map(int, input().split())


graph = defaultdict(list)
for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def is_star():
    star = True
    edge = 0
    center = 0
    for i in range(1, n + 1):
        if len(graph[i]) == 1:
            edge += 1
        elif len(graph[i]) == n - 1:
            center += 1
    return star and edge == n - 1 and center == 1

def is_bus():
    edge = 0
    bus = True
    for i in range(1, n + 1):
        if len(graph[i]) > 2:
            bus = False
            break
        elif len(graph[i]) == 1:
            edge += 1
    
    return bus and edge == 2 and n == e + 1


def is_ring():
    ring = True
    for i in range(1, n + 1):
        if len(graph[i]) != 2:
            ring = False
    
    return ring and n == e

if is_ring():
    print("ring topology")
elif is_star():
    print("star topology")
elif is_bus():
    print("bus topology")
else:
    print("unknown topology")