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

class QueueNode {
    
    dataMap: Record<number, any>;
    frontIndex: number;
    backIndex: number;
    
    constructor() {
        this.dataMap = {}
        this.frontIndex = 0;
        this.backIndex = 0;
    }

    enqueue(val: any) {
        this.dataMap[this.backIndex] = val;
        this.backIndex++;
    }
    dequeue() {
        const item = this.dataMap[this.frontIndex];
        delete this.dataMap[this.frontIndex];
        this.frontIndex++;
        return item;
    }
    length() {
        return this.backIndex - this.frontIndex;
    }
}

function levelOrder(root: TreeNode | null): number[][] {
    const queue = new QueueNode();
    const result: number[][] = [];
    
    if(root) {
    queue.enqueue(root);
        
    }
    
    while(queue.length() > 0) {
        const arr: number[] = [];
        const length =  queue.length()
        
        for(let i = 0; i<length; i++) {
            const cur = queue.dequeue();
            arr.push(cur.val)
            if(cur.left) {
                queue.enqueue(cur.left)
            }
            if(cur.right) {
                queue.enqueue(cur.right)
            }
        }
        result.push(arr)
    }
    return result
};

