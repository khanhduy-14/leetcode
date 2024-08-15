/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function reverseList(head: ListNode | null): ListNode | null {
    let prev = null;
    let curr = head;
    let newHead = head;
    while(curr){
        newHead = curr; 
        const nextCurr = curr.next; 
        newHead.next = prev; 
        prev = curr; 
        curr = nextCurr;
        
    }
    return newHead
};