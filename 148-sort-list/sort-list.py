# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow,fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        rightHead = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(rightHead)
        return self.merge(left, right)

    def merge(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(-1)
        cur = res
        while left and right:
            if left.val >= right.val:
                cur.next = right
                right = right.next
            else:
                cur.next = left
                left = left.next
            cur = cur.next
        if left:
            cur.next = left
        if right:
            cur.next = right
        return res.next
        
        



        
        
        