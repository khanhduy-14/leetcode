# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # no node
        if not head:
            return head
        
        new_tail = head
        old_tail = head 

        n = 1
        while old_tail.next:
            n+=1
            old_tail = old_tail.next
        
        step = k % n

        # modulo/no steps
        if step == 0:
            return head

        # connect tail to head/make the cycle
        old_tail.next = head

        # find the split index
        split_index = n - step - 1

        while split_index > 0:
            new_tail = new_tail.next 
            split_index-=1


        #remove the cycle
        result = new_tail.next
        new_tail.next = None

        return result
        
        
        

