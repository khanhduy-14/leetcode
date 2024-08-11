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

function maxDepth(root: TreeNode | null): number {
    
    let leftDepth = 0;
    let rightDepth = 0;
    if(!root) return 0;
    if (!root?.left && !root?.right) {
        return 1;
    }
    
    if (root?.left) {
        leftDepth += maxDepth(root.left);
    }
    
    if(root?.right) {
         rightDepth += maxDepth(root.right);
    }
    
    if(leftDepth > rightDepth) {
       return 1 + leftDepth;
    }
    
    return 1 + rightDepth
    
};