class Solution:
    def invertTree(self, root):
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root


''' Here is the explanation for the code above:
    1. If root is not None,
        set root.left to self.invertTree(root.right), and set root.right to self.invertTree(root.left). Then return root.
'''
