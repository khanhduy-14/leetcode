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

function isValidBST(root: TreeNode | null): boolean {
   return checkValidBST(root)
};

function checkValidBST(root: TreeNode | null, min: number = null, max: number = null) {
   if(!root) return true;
   if (min !==null && root.val <= min) {
       return false
   }
   if (max !== null && root.val >= max) {
       return false
   }
   let isValidLeft:boolean = true;
   let isValidRight:boolean = true;
    
   if(root.left){
      isValidLeft=checkValidBST(root.left, min, root.val)
   }
     if(root.right){
       isValidRight=checkValidBST(root.right, root.val, max)
   }
    return isValidLeft && isValidRight
    
}

