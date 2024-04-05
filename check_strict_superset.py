a = set(map(int, input().split()))
n = int(input())
sets = []
for i in range(2):
    new_set = set(map(int, input().split()))
    sets.append(new_set)

is_superset = True
for elem_set in sets:
    if not (a.issuperset(elem_set) and not a.issubset(elem_set)):
        is_superset = False
        break

print(is_superset)