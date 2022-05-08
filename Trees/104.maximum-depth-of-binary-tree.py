class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

''' Here is the explanation for the code above:
    1. If root is None, return 0.
    2. If root is not None,
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1.
'''
