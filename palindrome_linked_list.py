# https://leetcode.com/explore/featured/card/top-interview-questions-easy/93/linked-list/772/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
            
        return arr == arr[::-1]
     
