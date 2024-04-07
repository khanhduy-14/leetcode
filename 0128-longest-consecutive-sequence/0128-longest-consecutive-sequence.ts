function longestConsecutive(nums: number[]): number {
    const map  = {}
    let numLongestConsecutive = 0;
    for (let i = 0; i < nums.length; i++) {
            if(map[nums[i]]) continue;
            let lengthConsecutive = 1;
            const left = map[nums[i] - 1] ?? 0;
            const right = map[nums[i] + 1] ?? 0;
            lengthConsecutive = lengthConsecutive + left + right;
        
            map[nums[i]] = lengthConsecutive
            map[nums[i] -  left] = lengthConsecutive
            map[nums[i] +  right] = lengthConsecutive
        
            if (lengthConsecutive > numLongestConsecutive) {
                numLongestConsecutive = lengthConsecutive
            }
          
    }

    return numLongestConsecutive;
};