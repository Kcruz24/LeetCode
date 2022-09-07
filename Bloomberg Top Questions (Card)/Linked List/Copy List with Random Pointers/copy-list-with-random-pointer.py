from typing import Optional

class Node:
    def __init__(self, val=0):
        self.val
        self.next = None
        self.random = None


 # From LeetCode
 # O(N) Time | O(N) Space - Iterative
class Solution:
    def __init__(self):
        # Creating a visited dictionary to hold old node reference as "key" and new node reference as the "value"
        self.visited = {}

    def getClonedNode(self, node):
        # If node exists then
        if node:
            # Check if its in the visited dictionary
            if node in self.visited:
                # If its in the visited dictionary then return the new node reference from the dictionary
                return self.visited[node]
            else:
                # Otherwise create a new node, save the reference in the visited dictionary and return it.
                self.visited[node] = Node(node.val, None, None)
                return self.visited[node]
        return None


    def copyRandomList(self, head):
        if not head:
            return head

        old_node = head
        # Creating the new head node.
        new_node = Node(old_node.val, None, None)
        self.visited[old_node] = new_node

        # Iterate on the linked list until all nodes are cloned.
        while old_node != None:

            # Get the clones of the nodes referenced by random and next pointers.
            new_node.random = self.getClonedNode(old_node.random)
            new_node.next = self.getClonedNode(old_node.next)

            # Move one step ahead in the linked list.
            old_node = old_node.next
            new_node = new_node.next

        return self.visited[head]

# From LeetCode
# O(N) Time | O(N) Space - Recursive
class Solution2:
    def __init__(self):
        # Holds Old nodes as keys and new nodes as values
        self.visited_hash = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if head == None:
            return None

        # If we have already processed the current node, we return the cloned version of it.
        if head in self.visited_hash:
            return self.visited_hash[head]

        # Create new node with the value of the old node
        node = Node(head.val)

        # This helps to avoid cycles
        self.visited_hash[head] = node

        # Traverse starting from the next and random pointers
        # Finally update the next and random pointers for the new node created
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node

# From LeetCode
# O(N) Time | (1) Space - Iterative
class Solution3:
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head

        # Creating a new weaved list of original and copied nodes.
        ptr = head
        while ptr:

            # Cloned node
            new_node = Node(ptr.val, None, None)

            # Inserting the cloned node just next to the original node.
            # If A->B->C is the original linked list,
            # Linked list after weaving cloned nodes would be A->A'->B->B'->C->C'
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next

        ptr = head

        # Now link the random pointers of the new nodes created.
        # Iterate the newly created list and use the original nodes random pointers,
        # to assign references to random pointers for cloned nodes.
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next

        # Unweave the linked list to get back the original linked list and the cloned list.
        # i.e. A->A'->B->B'->C->C' would be broken to A->B->C and A'->B'->C'
        ptr_old_list = head  # A->B->C
        ptr_new_list = head.next  # A'->B'->C'
        head_new = head.next
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next
        return head_new
