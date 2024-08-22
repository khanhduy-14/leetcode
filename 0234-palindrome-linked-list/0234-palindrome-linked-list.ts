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

function isPalindrome(head: ListNode | null): boolean {
    let slow: ListNode = head;
    let fast: ListNode = head;
    let prev = null;
    let temp = null;
    
    while(fast && fast.next) {
        slow = slow.next;
        fast = fast.next;
            fast= fast.next
    }
    prev = slow;
    slow= slow.next;
    prev.next = null;
    while(slow) {
        temp = slow.next;
        slow.next = prev;
        prev = slow;
        slow = temp;
    }
    fast = head; slow = prev;
    while(slow) {
        if(slow?.val !== fast?.val) {
            return false;
        }
        slow = slow.next
        fast = fast.next
    }
    return true;
};