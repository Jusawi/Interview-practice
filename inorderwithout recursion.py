def inOrder(root): 
      
    # Set current to root of binary tree 
    current = root  
    s = [] # initialze stack 
    done = 0 
      
    while(not done): 
          
        # Reach the left most Node of the current Node 
        if current is not None: 
              
            # Place pointer to a tree node on the stack  
            # before traversing the node's left subtree 
            s.append(current) 
          
            current = current.left  
  
          
        # BackTrack from the empty subtree and visit the Node 
        # at the top of the stack; however, if the stack is  
        # empty you are done 
        else: 
            if(len(s) >0 ): 
                current = s.pop() 
                print current.data, 
          
                # We have visited the node and its left  
                # subtree. Now, it's right subtree's turn 
                current = current.right  
  
            else: 
                done = 1
       
       
       
 def iterativePreorder(root): 
      
    # Base CAse  
    if root is None: 
        return 
  
    # create an empty stack and push root to it 
    nodeStack = [] 
    nodeStack.append(root) 
  
    #  Pop all items one by one. Do following for every popped item 
    #   a) print it 
    #   b) push its right child 
    #   c) push its left child 
    # Note that right child is pushed first so that left 
    # is processed first */ 
    while(len(nodeStack) > 0): 
          
        # Pop the top item from stack and print it 
        node = nodeStack.pop() 
        print node.data, 
          
        # Push right and left children of the popped node 
        # to stack 
        if node.right is not None: 
            nodeStack.append(node.right) 
        if node.left is not None: 
            nodeStack.append(node.left) 
