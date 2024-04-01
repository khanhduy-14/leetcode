/**
 Do not return anything, modify nums in-place instead.
 */
function moveZeroes(nums: number[]): void {
    
    if(nums.length>=2){
        
    let j: number =  0;
    
    for (let i = 0; i < nums.length; i++) {
      if (nums[i]!==0) {
         [nums[j], nums[i]] = [nums[i], nums[j]];
         j++;
          
      }
    }
    }
        

};