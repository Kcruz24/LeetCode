# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # O(N) Time | O(N) Space
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def get_parents(node, parent, parents):
            if node:
                parents[node.val] = parent
                get_parents(node.left, node, parents)
                get_parents(node.right, node, parents)

            return parents

        def get_ancestors(node):
            ancestors = set()

            while node:
                ancestors.add(node.val)
                node = parents[node.val]

            return ancestors

        def find_lca(node):
            while node:
                if node.val in p_ancestors:
                    return node

                node = parents[node.val]

        parents = get_parents(root, None, {})
        p_ancestors = get_ancestors(p)
        lca = find_lca(q)

        return lca
