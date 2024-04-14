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

function hasCycle(head: ListNode | null): boolean {
    let cursor = head;
    while(cursor !== null ) {
        if(cursor.val === Number.MAX_VALUE) {
            return true;
        }
        cursor.val = Number.MAX_VALUE;
        cursor =  cursor.next;
    }
    return false
};