"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def recur(node):
            pre,traverser = node,node
            while traverser:
                pre = traverser
                if traverser.child:
                    tobenext,tobeend  = recur(traverser.child)
                    traverser.child = None
                    tobenext.prev = traverser
                    tobeend.next = traverser.next
                    if traverser.next:
                        traverser.next.prev = tobeend
                    traverser.next = tobenext
                traverser = traverser.next
            return node,pre

        return recur(head)[0]

