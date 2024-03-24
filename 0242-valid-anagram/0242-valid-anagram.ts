function isAnagram(s: string, t: string): boolean {
    if(s.length !== t.length)  return false;
    const map = new Map<string, number>();
    
    for(let i=0; i<s.length; i++) {
        if(map.has(s[i])) {
            const numLetter = map.get(s[i]) + 1;
            map.set(s[i], numLetter)
        }
        else {
            map.set(s[i], 1)
        }
    }
     for(let i=0; i<t.length; i++) {
        if(map.get(t[i]) > 0) {
               const numLetter = map.get(t[i]) - 1;
                map.set(t[i], numLetter)
        }
        else {
            return false;
        }
    }
    return true;
};