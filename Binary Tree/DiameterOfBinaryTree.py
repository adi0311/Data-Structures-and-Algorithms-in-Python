"""
    Diameter of a binary tree is the maximum distance
    between any pair of nodes.
"""
from collections import deque


class BinaryTree:
    class Node:
        def __init__(self, val=0, left=None, right=None):
            self.data = val
            self.left = left
            self.right = right

    class Height:
        def __init__(self, h=0):
            self.height = h

        def __add__(self, other):
            return self.height + other.height

    def __init__(self, data):
        self.root = self.deserialize(data)

    def deserialize(self, data):
        if not data:
            return
        arr = data.split()
        n = len(arr)
        root = self.Node(arr[0])
        d = deque()
        d.append(root)
        i = 1
        while d and i < n:
            temp = d.popleft()
            if arr[i] == 'no':
                temp.left = None
            else:
                temp.left = self.Node(arr[i])
                d.append(temp.left)
            i += 1
            if i < n:
                if arr[i] == 'no':
                    temp.right = None
                else:
                    temp.right = self.Node(arr[i])
                    d.append(temp.right)
            i += 1
        return root

    def height(self, root):
        if not root:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1

    def diameter_n_square(self, root):
        if not root:
            return 0
        return max(self.diameter_n_square(root.left),
                   self.diameter_n_square(root.right),
                   self.height(root.left) + self.height(root.right) + 1
                   )

    def diameter_in_n(self, root, height):
        if not root:
            height.height = 0
            return 0
        leftest, rightest = self.Height(), self.Height()
        left_diameter, right_diameter = self.diameter_in_n(root.left, leftest), self.diameter_in_n(root.right, rightest)
        height.height = max(leftest.height, rightest.height) + 1
        return max(left_diameter, right_diameter, leftest + rightest + 1)

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.data, end=" ")
            self.inorder_traversal(root.right)


tree_arr = "1 2 3 4 5 6 7 8 9 10 no no no no no"
bt = BinaryTree(tree_arr)
print(bt.diameter_n_square(bt.root))
print(bt.diameter_in_n(bt.root, bt.Height()))
