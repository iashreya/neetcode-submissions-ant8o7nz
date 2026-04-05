"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None

        temp = head.next
        node = Node(head.val, None, None)
        copy = node
        while (temp):
            new_node = Node(temp.val, temp.next, None)
            node.next = new_node
            node = new_node
            temp = temp.next

        temp = copy
        array = []
        while(temp):
            array.append(temp)
            temp = temp.next


        temp = head
        h_map = {} 
        count = 0
        while(temp):
            h_map[temp] = count
            temp = temp.next
            count += 1
        

        temp = head
        for node in array:
            if temp.random != None:
                node.random = array[h_map[temp.random]]
            else:
                node.random = None
            temp = temp.next

        return copy

        
        
            