# https://leetcode.com/explore/featured/card/top-interview-questions-easy/93/linked-list/560/

# Solution


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = None
        while head:
            if not newHead:
                newHead = ListNode(head.val)
            else:
                newNode = ListNode(head.val)
                newNode.next = newHead
                newHead = newNode
            head = head.next
    
        return newHead
            
