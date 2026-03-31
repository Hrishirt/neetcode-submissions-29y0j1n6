# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:    
        prev, curr = None, head
        while curr:
            temp = curr.next # 1 2 
            curr.next = prev # None 1
            prev = curr # 0 1
            curr = temp # 1 2
        return prev
    