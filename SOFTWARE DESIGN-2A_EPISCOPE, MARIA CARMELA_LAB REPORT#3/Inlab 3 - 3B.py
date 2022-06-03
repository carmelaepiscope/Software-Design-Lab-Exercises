# Binary search tree recursively in pre-order, post-order and in-order
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val),
        printInorder(root.right)
 
def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val),
 
def printPreorder(root):
    if root:
        print(root.val),
        printPreorder(root.left)
        printPreorder(root.right)
 
root = Node(12)
root.left = Node(25)
root.right = Node(27)
root.left.left = Node(22)
root.left.right = Node(14)

print ("Preorder traversal of binary tree are: ")
printPreorder(root)
 
print ("\nInorder traversal of binary tree are: ")
printInorder(root)
 
print ("\nPostorder traversal of binary tree are: ")
printPostorder(root)