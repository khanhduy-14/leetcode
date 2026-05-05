# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        

        new_tail = head
        tail = head 

        n = 1
        while tail.next:
            n+=1
            tail = tail.next
        
      
        print(n)
        step = k % n

        if step == 0:
            return head

        tail.next = head
        split_index = n - step - 1

        while split_index > 0:
            new_tail = new_tail.next 
            split_index-=1
        
        result = new_tail.next
        new_tail.next = None

        return result
        
        
        

