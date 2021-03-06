def hasPathSum(self, root, sum):
        if not root:
            return False

        if not root.left and not root.right and root.val == sum: #if leaf node
            return True
        
        sum -= root.val

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
