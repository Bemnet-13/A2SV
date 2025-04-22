# Problem: Cyclic Components - https://codeforces.com/problemset/problem/977/E

from collections import defaultdict
import sys
import threading

input_fn = lambda: sys.stdin.readline().strip()

def main():
    n, m = map(int, input().split())
    graph = defaultdict(list)

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [False for _ in range(n + 1)]

    def dfs(start, nodes, curr):

        visited[curr] = True
        if len(graph[curr]) >= 3:
            return False

        for neighbor in graph[curr]:
            if not visited[neighbor]:
                return dfs(start, nodes + 1, neighbor)
            elif visited[neighbor] and neighbor == start and nodes >= 3:
                return True
        
        return False
            

    count = 0
    for i in range(1, n + 1):
        if not visited[i]:
            is_cycle = dfs(i, 1, i)
            if is_cycle:
                count += 1

    print(count)

if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()