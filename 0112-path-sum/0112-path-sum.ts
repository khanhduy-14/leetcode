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

function hasPathSum(root: TreeNode | null, targetSum: number): boolean {
       if(!root) {
            return false;
        }
    
    const backtracking = (root: TreeNode, curr: number) => {
   
     if(!root.left && !root.right){
         if(curr === targetSum) {
             return true;
         }
         return false;
     }
  
     
     if(root.left) {
        if(backtracking(root.left, curr + root.left.val)){
            return true;
        }
     }   
     if(root.right) {
         if(backtracking(root.right, curr + root.right.val)){
            return true;
        }
     }
        return false;
        
     
    }
    if(backtracking(root, root.val)) return true;
    return false;
}