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

console.log(getGroupKeyByWord('abbbbbbbbbbb'))
console.log(getGroupKeyByWord("aaaaaaaaaaab"))
    function getGroupKeyByWord(word: string): string {    
    const arr = Array.from({length: 26},()=>0);
    let key = ''
    for(let i=0;i<word.length;i++) {
        arr[word.charCodeAt(i)-97]+=1;
    }
      for(let i=0;i<arr.length;i++) {
        if(arr[i]>0){
            key = key+String(i) + String(arr[i]) + '|'
        }
    }
    return key
}