# Problem: Fox And Names  (codeforces) - https://codeforces.com/contest/510/problem/C

from collections import defaultdict

n = int(input())
store = []
longest = 0

for _ in range(n):
    s = input()
    longest = max(longest, len(s))
    store.append(s)

graph = defaultdict(set)

similar = set()
possible = True

for i in range(longest):
    for word_pos in range(n):
        if i >= len(store[word_pos]):
            continue
        curr_letter = store[word_pos][i]
        prev_strip = store[word_pos][:i]
        for k in range(word_pos + 1, n):
            curr_strip = store[k][:i]
            if i < len(store[k]) and curr_letter != store[k][i] and prev_strip == curr_strip:
                graph[curr_letter].add(store[k][i])
            elif prev_strip == curr_strip and i >= len(store[k]):
                possible = False


order = []
colors = [0 for _ in range(26)]

def topSort(node):
    global order
    global colors

    if colors[node] == 1:
        return False

    colors[node] = 1

    letter = chr(node + 97)
    for neighbor in graph[letter]:
        node_neighbor = ord(neighbor) - 97
        if colors[node_neighbor] == 2:
            continue
        if not topSort(node_neighbor):
            return False
    
    colors[node] = 2
    order.append(letter)
    return True

for i in range(26):
    if colors[i] == 0:
        possible = possible and topSort(i)

if possible:
    ans = "".join(order[::-1])
    print(ans)
else:
    print("Impossible")