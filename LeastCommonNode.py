#LCA in Binary SEarch Tree
def lca(root, n1, n2): 
      
    # Base Case 
    if root is None: 
        return None
  
    # If both n1 and n2 are smaller than root, then LCA 
    # lies in left 
    if(root.data > n1 and root.data > n2): 
        return lca(root.left, n1, n2) 
  
    # If both n1 and n2 are greater than root, then LCA 
    # lies in right  
    if(root.data < n1 and root.data < n2): 
        return lca(root.right, n1, n2) 
  
    return root 

#LCA in Binary tree

'''Following is simple O(n) algorithm to find LCA of n1 and n2.
1) Find path from root to n1 and store it in a vector or array.
2) Find path from root to n2 and store it in another vector or array.
3) Traverse both paths till the values in arrays are same. Return the common element just before the mismatch.
'''
# Finds the path from root node to given root of the tree. 
# Stores the path in a list path[], returns true if path  
# exists otherwise false 
def findPath( root, path, k): 
  
    # Baes Case 
    if root is None: 
        return False
  
    # Store this node is path vector. The node will be 
    # removed if not in path from root to k 
    path.append(root.key) 
  
    # See if the k is same as root's key 
    if root.key == k : 
        return True
  
    # Check if k is found in left or right sub-tree 
    if ((root.left != None and findPath(root.left, path, k)) or
            (root.right!= None and findPath(root.right, path, k))): 
        return True 
  
    # If not present in subtree rooted with root, remove 
    # root from path and return False 
       
    path.pop() 
    return False
  
# Returns LCA if node n1 , n2 are present in the given 
# binary tre otherwise return -1 
def findLCA(root, n1, n2): 
  
    # To store paths to n1 and n2 fromthe root 
    path1 = [] 
    path2 = [] 
  
    # Find paths from root to n1 and root to n2. 
    # If either n1 or n2 is not present , return -1  
    if (not findPath(root, path1, n1) or not findPath(root, path2, n2)): 
        return -1 
  
    # Compare the paths to get the first different value 
    i = 0 
    while(i < len(path1) and i < len(path2)): 
        if path1[i] != path2[i]: 
            break
        i += 1
    return path1[i-1] 
  
