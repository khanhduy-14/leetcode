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

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    const resultNode = new ListNode();
    let curResultNode = resultNode;
    let carry = 0;
    while(l1 || l2) {
        let sum = 0;
        if(l1) {
            sum += l1.val;
            l1 = l1.next;
        }
         if(l2) {
            sum += l2.val;
            l2 = l2.next;
        }
        const result = (sum + carry) % 10;
        carry = Math.floor((sum + carry) / 10);
        console.log(carry)
        curResultNode.next = new ListNode(result);
        curResultNode = curResultNode.next;
    }
    if(carry > 0) {
        curResultNode.next = new ListNode(carry);
    }        
    return resultNode.next
};