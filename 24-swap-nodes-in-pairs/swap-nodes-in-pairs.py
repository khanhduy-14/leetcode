# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        
        nf = dummy.next
        if not nf:
            return head
        ns = dummy.next.next
        if not ns:
            return head
        nas = ns.next
        dummy.next = ns
        ns.next = nf
        
            

        nf.next = self.swapPairs(nas)
        return dummy.next