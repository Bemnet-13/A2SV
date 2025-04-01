# Problem: Christmas Spruce - https://codeforces.com/contest/913/problem/B

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

nodes = { 1: TreeNode(1)}

n = int(input())
for i in range(2, n + 1):
    parent = int(input())
    child_node = TreeNode(i)
    nodes[i] = child_node
    parent_node = nodes.get(parent, -1)
    parent_node.children.append(child_node)

ans = True
def inorder(node):
    
    count = 0
    for child_node in node.children:
        if not child_node.children:
            count += 1
        else:
            inorder(child_node)
    
    global ans
    ans = ans and count >= 3

inorder(nodes[1])
if ans:
    print("Yes")
else:
    print("No")
