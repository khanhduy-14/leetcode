function productExceptSelf(nums: number[]): number[] {
    const result: number[] = [];
    let left = 1;
    let right = 1;
    for(let i=0;i < nums.length;i++){
        result[i] = left;
        left *= nums[i]
    }
    
       for(let i=nums.length - 1;i >= 0;i--){
        result[i] *= right;
        right *= nums[i]
    }
    return result
    
};