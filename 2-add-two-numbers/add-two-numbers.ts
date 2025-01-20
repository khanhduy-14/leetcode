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
    while(l1 || l2 || carry > 0) {
        let sum = carry;
        if(l1) {
            sum += l1.val;
            l1 = l1.next;
        }
         if(l2) {
            sum += l2.val;
            l2 = l2.next;
        }
        const result =sum % 10;
        carry = Math.floor(sum / 10);
        curResultNode.next = new ListNode(result);
        curResultNode = curResultNode.next;
    }
   
    return resultNode.next
};