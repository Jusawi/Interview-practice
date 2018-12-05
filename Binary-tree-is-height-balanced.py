'''From the definition of a balanced tree, we can conclude that a binary tree is balanced if:

1- the right subtree is balanced

2- the left subtree is balanced

3- the difference between the height of the left subtree and the right subtree is at most 1'''

def get_height(root):
    if root is None: 
        return 0
    return 1 + max(get_height(root.left)\
    , get_height(root.right))

def is_balanced(root):
    # a None tree is balanced
    if root is None: 
        return True
    return is_balanced(root.right) and \
    is_balanced(root.left) and \
    abs(get_height(root.left) - get_height(root.right)) <= 1
