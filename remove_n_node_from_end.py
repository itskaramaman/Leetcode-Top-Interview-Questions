# https://leetcode.com/explore/featured/card/top-interview-questions-easy/93/linked-list/603/

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        slow_pointer = head
        fast_pointer = head
        i = 0
        while i < n:
            fast_pointer = fast_pointer.next
            i += 1
            
        while fast_pointer != None:
            prev = slow_pointer
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next
            
        if prev == None and slow_pointer == head:
            head = head.next
            return head
        if prev.next:
            prev.next = prev.next.next
        else:
            prev = None
        
        return head
            
