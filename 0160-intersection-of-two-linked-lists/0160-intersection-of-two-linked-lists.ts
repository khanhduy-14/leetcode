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

function getIntersectionNode(headA: ListNode | null, headB: ListNode | null): ListNode | null {
    const setNode = new Set<ListNode>();
    
    let curA = headA
    let curB = headB
    while (curA !== null) {
        setNode.add(curA);
        curA = curA.next;
    }
    while (curB !== null) {
        if(setNode.has(curB)) {
            return curB
        }
        curB = curB.next;
    }
    return null
};