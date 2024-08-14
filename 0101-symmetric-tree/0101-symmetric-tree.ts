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

function isSymmetric(root: TreeNode | null): boolean {

    if(!root) return true;
    
    return isSubtreeSymmetric(root.left, root.right);
};

function isSubtreeSymmetric(leftTree: TreeNode, rightTree: TreeNode): boolean { 
    if(!leftTree && !rightTree) {
        return true;
    }
    if(!leftTree || !rightTree) {
        return false;
    }
    if(leftTree.val === rightTree.val) {
        return isSubtreeSymmetric(leftTree.left, rightTree.right) &&  isSubtreeSymmetric(leftTree.right, rightTree.left)
    }
     return false;
}