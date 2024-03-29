function singleNumber(nums: number[]): number {
    const mapFrq: Record<number, boolean> = {};
    let output = nums[0];
    mapFrq[nums[0]] = true;
    for(let i=1; i < nums.length; i++) {
        if(mapFrq[nums[i]]) {
            output -= nums[i]
        }
        else {
            output += nums[i]
            mapFrq[nums[i]] = true;
        }
    }
    return output;
};