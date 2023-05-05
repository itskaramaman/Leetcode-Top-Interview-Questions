# https://leetcode.com/explore/featured/card/top-interview-questions-easy/93/linked-list/771/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = None
        result = None
        
        if not list1 and not list2:
            return None
        
        if not list1:
            return list2
        
        if not list2:
            return list1
        
        if list1.val < list2.val:
            result = list1
            list1 = list1.next
        else:
            result = list2
            list2 = list2.next
            
        newHead = result
        result.next = None
        
        while list1 and list2:
            if list1.val < list2.val:
                result.next = list1
                result = result.next
                list1 = list1.next
            else:
                result.next = list2
                result = result.next
                list2 = list2.next
    
        if list1:
            result.next = list1
        if list2:
            result.next = list2
            
        return newHead
    
