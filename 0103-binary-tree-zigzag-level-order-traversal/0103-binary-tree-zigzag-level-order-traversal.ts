/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function zigzagLevelOrder(root: TreeNode | null): number[][] {
    const result: number[][] = [];
    const queue: TreeNode[] = [];
    if(root) {
        queue.push(root)
    }
   let level = 1;
    
    while(queue.length > 0) {
        const lengthQueue = queue.length;
        const breadth = [];
        for(let i=0; i < lengthQueue; i++) {
            const cur = queue.shift();
            if(level % 2 === 1) {
            breadth.push(cur.val);
            }
            else {
            breadth.unshift(cur.val);
                
            }
                if(cur.left) {
                   queue.push(cur.left);
                }
                 if(cur.right) {
                queue.push(cur.right);
                }
                

        }
        level++;
        result.push(breadth);
    }
    return result
};