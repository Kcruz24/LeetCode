# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''


if p and q in right_subtree:
    search right_subtree
if p and q in left_subtree:
    search left_subtree
if p and q not in right_subtree and left_subtree:
    return current node

'''

class Solution:
    # O(N) Time | O(N) Space
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent_val = root.val

        p_val = p.val
        q_val = q.val

        if p_val > parent_val and q_val > parent_val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p_val < parent_val and q_val < parent_val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root


class Solution2:
    # O(N) Time | O(1) Space
    def lowestCommonAncestor(self, root, p, q):

        trav = root
        while trav:
            parent_val = trav.val

            if p.val > parent_val and q.val > parent_val:
                trav = trav.right
            elif p.val < parent_val and q.val < parent_val:
                trav = trav.left
            else:
                return trav

