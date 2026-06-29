# Binary Tree Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sum_nodes(root):
    if root is None:
        return 0
    return root.data + sum_nodes(root.left) + sum_nodes(root.right)


root = Node(10)
root.left = Node(5)
root.right = Node(15)

print("Sum of all nodes:", sum_nodes(root))