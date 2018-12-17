# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        first = head
        second = head
        for _ in range(n):
            first = first.next
            
        if first is None:
            head = head.next
            return head
        while(first.next != None):
            first = first.next
            second = second.next
        second.next = second.next.next
        return head
