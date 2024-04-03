function groupAnagrams(strs: string[]): string[][] {
    const mapSumCharCode = new Map<string, string[]>();
    const result: string[][] = []
    for(let i=0;i<strs.length;i++) {
        const sumCharCode = getGroupKeyByWord(strs[i]);
        if(mapSumCharCode.has(sumCharCode)) {
            const words = mapSumCharCode.get(sumCharCode);
            words.push(strs[i])
            mapSumCharCode.set(sumCharCode,words)
        }else {
            mapSumCharCode.set(sumCharCode,[strs[i]])
        }
    }
    
    for(let [key, value] of mapSumCharCode) {
        result.push(value)
    }
    return result
};

    function getGroupKeyByWord(word: string): string {    
    return  [...word].sort().join("")
}