function productExceptSelf(nums: number[]): number[] {
    let numZero : number = 0;
    let multi =  1;
    
    
    for(let i = 0; i < nums.length; i++) {
        if(nums[i]!==0) {
             multi *= nums[i]
        }
        else {
            numZero+=1;
        }
       
    }
    if (numZero >= 2) {
        return Array(nums.length).fill(0);
    }
    const result: number[] = [];
    
    for(let i = 0; i < nums.length; i++) {
        if(numZero === 1) {
             if(nums[i]!==0){
                 result.push(0)
             }
            else {
                result.push(multi)
            }
        }
        else {
            result.push(multi / nums[i])
        }
       
    }
    return result
    
};