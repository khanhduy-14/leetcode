function intersect(nums1: number[], nums2: number[]): number[] {
    const result: number[] = [];
    
    const mapFrq: Record<number, number> = {}
    const smallArray = nums1.length < nums2.length ? nums1 : nums2;
    const largeArray = nums1.length >= nums2.length ? nums1 : nums2;
    
    
    for(let i=0; i < smallArray.length;i++) {
        if(mapFrq[smallArray[i]]) {
            mapFrq[smallArray[i]]+=1;
        }
        else{
            mapFrq[smallArray[i]]=1;
        }
    } 
    
        for(let i=0; i < largeArray.length;i++) {
        if(mapFrq[largeArray[i]] && mapFrq[largeArray[i]]>0) {
             result.push(largeArray[i])
             mapFrq[largeArray[i]]-=1;
        }
    } 
    return result;
};