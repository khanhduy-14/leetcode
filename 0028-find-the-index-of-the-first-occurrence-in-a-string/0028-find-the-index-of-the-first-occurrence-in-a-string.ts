function strStr(haystack: string, needle: string): number {
    for(let i = 0; i< haystack.length; i++) {
        let isSameText = true;
        for(let j=0; j< needle.length;j++) {
            if(haystack[i+j] !== needle[j]) {
                isSameText = false;
            }
       
        }
             if(isSameText) {
                return i;
            }
    }
    return -1
};