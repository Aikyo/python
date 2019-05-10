class Node:
    def __init__(self,value=None,left=None,right=None):
        self.value = value
        self.right = right
        self.left = left

def preTraverse(root):
    if root == None:
        return
    print(root.value)
    preTraverse(root.left)
    preTraverse(root.right)

def midTraverse(root):
    if root == None:
        return
    midTraverse(root.left)
    print(root.value)
    midTraverse(root.right)
