function missingNumber(nums: number[]): number {
    let sum = (nums.length + 1) * nums.length / 2;
    for(const num of nums) {
        sum-=num
    }
    return sum;
};