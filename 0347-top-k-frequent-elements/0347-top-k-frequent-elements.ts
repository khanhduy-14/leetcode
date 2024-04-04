function topKFrequent(nums: number[], k: number): number[] {
    const mapFreq = new Map<number, number>();
    
    for(let i=0;i<nums.length;i++) {
        const freqInMap = mapFreq.get(nums[i])
        if(freqInMap) {
            mapFreq.set(nums[i] , freqInMap+1)
        }
        else {
             mapFreq.set(nums[i] , 1)
        }
    }
    const array = [];
    for(let [key, value] of mapFreq) {
       array.push(key);
    }
    array.sort((a,b) => mapFreq.get(b) - mapFreq.get(a))
    return array.slice(0, k)
};
