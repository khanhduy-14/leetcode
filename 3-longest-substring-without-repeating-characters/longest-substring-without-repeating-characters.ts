function lengthOfLongestSubstring(s: string): number {
    let substring = '';
    let maxSubstring = '';
    const distinctCharacterIndexMap: Record<string, number> = {};
   
    for(let i = 0; i < s.length; i++) {
        if(distinctCharacterIndexMap[s[i]] !== undefined && distinctCharacterIndexMap[s[i]] !== -1){
           const dupCharacterIndex = substring.indexOf(s[i]);
           substring = substring.slice(dupCharacterIndex + 1);
             distinctCharacterIndexMap[s[i]] = -1;
        }
        distinctCharacterIndexMap[s[i]] = 1;
        substring += s[i]
        if (substring.length > maxSubstring.length) {
            maxSubstring = substring;
        }
    }
    return maxSubstring.length
};