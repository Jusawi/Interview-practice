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


#Better Method
def is_balanced_helper(root):
    # a None tree is balanced
    if root is None:
        return 0
    left_height = is_balanced_helper(root.left)
    # if the left subtree is not balanced, then:
    # this tree is also not balanced
    if left_height == -1:
        return -1
    # if the right subtree is not balanced, then:
    # this tree is also not balanced
    right_height = is_balanced_helper(root.right)
    if right_height == -1:
        return -1
    # if the diffrence in heights is greater than 1, then:
    # this tree is not balanced
    if abs(left_height - right_height) > 1:
        return -1
    # this tree is balanced, return its height
    return max(left_height, right_height) + 1
