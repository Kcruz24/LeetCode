from typing import List, Optional


class Tree:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


def preOrderTraversal(tree, array=[]):
    if tree is None:
        return

    print(tree.value)
    preOrderTraversal(tree.left)
    preOrderTraversal(tree.right)


def inOrderTraversal(tree, array=[]):
    if tree is None:
        return

    inOrderTraversal(tree.left)
    array.append(tree.value)
    inOrderTraversal(tree.right)

    return array


# preOrder = [3, 9, 20, 15, 7]
# inOrder = [9, 3, 15, 20, 7]


# (N) time | O(N) space
def buildTree(preorder, inorder):
    if len(preorder) == 0:
        return None

    # This gives the root data
    rootData = preorder[0]
    root = Tree(rootData)
    # print("val", root.value)
    rootIdx = -1
    for i in range(len(inorder)):
        if rootData == inorder[i]:
            rootIdx = i
            break
    # rootIdx = 1
    if rootIdx == -1:
        return None

    # leftInorder = [9]
    # This gives the leftInorder
    leftInorder = inorder[:rootIdx]

    # rightInorder = [15, 20, 7]
    # This gives the rightInorder
    rightInorder = inorder[rootIdx + 1:]

    # lenLeftSubTree = 1
    lenLeftSubTree = len(leftInorder)

    # leftPreorder = 1:2
    leftPreorder = preorder[1:lenLeftSubTree + 1]
    print('leftPre', leftPreorder)
    rightPreorder = preorder[lenLeftSubTree + 1:]
    print('rightPre', rightPreorder)

    # Recursion will build the tree
    # Making connnections of the tree
    root.left = buildTree(leftPreorder, leftInorder)
    root.right = buildTree(rightPreorder, rightInorder)

    return root


class Solution:
    # O(N) time | O(N) space
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[Tree]:
        if not inorder:
            return None

        root = Tree(preorder.pop(0))
        root_idx = inorder.index(root.value)

        left_inorder = inorder[:root_idx]
        right_inorder = inorder[root_idx + 1:]

        root.left = self.buildTree(preorder, left_inorder)
        root.right = self.buildTree(preorder, right_inorder)

        return root


if __name__ == '__main__':
    root = Tree(3)
    root.left = Tree(9)
    root.right = Tree(20)
    root.right.left = Tree(15)
    root.right.right = Tree(7)

    preOrder = [3, 9, 20, 15, 7]
    inOrder = [9, 3, 15, 20, 7]

    sol = Solution()

    new_tree = sol.buildTree(preOrder, inOrder)

    new_preorder = preOrderTraversal(new_tree)
    preOrderTraversal(new_preorder)
