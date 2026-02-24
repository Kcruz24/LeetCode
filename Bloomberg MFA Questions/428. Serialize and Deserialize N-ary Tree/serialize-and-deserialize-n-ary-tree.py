
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        return {'value': root.val, 'children': [self.serialize(child) for child in root.children]} if root else {}

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        return Node(data['value'], [self.deserialize(child) for child in data['children']]) if data else None


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
