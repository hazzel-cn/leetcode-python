# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        current_ptr = head
        next_ptr = head.next

        while next_ptr is not None:
            if current_ptr.val == next_ptr.val:
                # delete
                current_ptr.next = next_ptr.next
                next_ptr = current_ptr.next
            else:
                current_ptr = next_ptr
                next_ptr = next_ptr.next
        return head




