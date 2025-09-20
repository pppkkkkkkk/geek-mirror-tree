'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def mirror(self, root):
        # Code here
        
        def rev(node):
            if not node:
                return
            
            rev(node.left)
            rev(node.right)
            
            left = node.left
            right = node.right
            
            node.left = right
            node.right = left
            
        rev(root)
        