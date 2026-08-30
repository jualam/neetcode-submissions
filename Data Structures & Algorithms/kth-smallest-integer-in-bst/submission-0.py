# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res=[]
        def traverse(curr_node):
            if curr_node is None:
                return 
            traverse(curr_node.left)
            res.append(curr_node.val)
            traverse(curr_node.right)
        
        traverse(root)
        return res[k-1]