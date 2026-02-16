from collections import deque

class TreeNode: 

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def getVal(self):
        return str(self.val)

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F


def pre_order(node):
    if not node:
        return
    
    print(node.getVal())
    pre_order(node.left)
    pre_order(node.right)

def pre_order_iterative(node):
    if not node:
        return
    stack = [node]
    while stack:
        current = stack.pop()
        print(current.getVal())
        if current.right: stack.append(current.right)
        if current.left: stack.append(current.left)
    

def in_order(node):
    if not node:
        return

    in_order(node.left)
    print(node.getVal())
    in_order(node.right)

def post_order(node):
    if not node:
        return
    post_order(node.left)
    post_order(node.right)
    print(node.getVal())

def level_order(node):
    if not node:
        return
    queue = deque([node])
    while queue:
        current = queue.popleft()
        print(current.getVal())
        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)
    return queue

print(f"Pre-order traversal: {pre_order(A)}")
print(f"In-order traversal: {in_order(A)}")
print(f"Post-order traversal: {post_order(A)}")

def search(node, target):
    if not node:
        return False
    if node.val == target:
        return True
    
    return search(node.left, target) or search(node.right, target)

def search_bst(node, target):
    if not node:
        return False
    if node.val == target:
        return True
    if target < node.val: search_bst(node.left, target)
    else: search_bst(node.right, target)
