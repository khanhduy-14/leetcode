# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head and head.next and head.next.next:
            first = head
            second = head.next
            last = head.next.next
            prev_last = head.next

            while last.next:
                prev_last = last
                last = last.next
  
            prev_last.next = None
            first.next = last
            last.next = second
            self.reorderList(second) 
