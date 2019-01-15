class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        tokens = []
        self._serialize(root, tokens)
		# Reverse the list to make it easy for decoding
		# Can be used as a stack and each element can be popped successively
		tokens = tokens[::-1]
        data = ' '.join(tokens)
        return data

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # Split data into list of tokens
		tokens = data.split(' ')
        return self._deserialize(tokens)

    def _serialize(self, root, tokens):
        if root is None:
            tokens.append('#')
            return
        tokens.append('%s' % root.val)
        self._serialize(root.left, tokens)
        self._serialize(root.right, tokens)

    def _deserialize(self, tokens):
        token = tokens.pop()
        if token == '#':
            return None
        node = TreeNode(int(token))
        node.left = self._deserialize(tokens)
        node.right = self._deserialize(tokens)
        return node
