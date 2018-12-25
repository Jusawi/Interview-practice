#Iterative
class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next: return head
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        
        while cur.next and cur.next.next:
            first = cur.next
            sec = cur.next.next
            cur.next = sec
            first.next = sec.next
            sec.next = first
            cur = cur.next.next
        return dummy.next       


#Recursive
class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next: return head
        new_start = head.next.next
        head, head.next = head.next, head
        head.next.next = self.swapPairs(new_start)
        return head
