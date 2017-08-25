# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        ptr = head
        while ptr.next != None:
            if ptr.next.val == val:
                self.littleRemove(ptr)
            ptr = ptr.next
        return head

        
    def littleRemove(self, node):
        node.val = node.next.val
        node.next = node.next.next