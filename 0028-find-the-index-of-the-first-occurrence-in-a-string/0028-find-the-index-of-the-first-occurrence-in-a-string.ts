function strStr(haystack: string, needle: string): number {
    for(let i = 0; i< haystack.length; i++) {
        for(let j=0; j< needle.length;j++) {
            if(haystack[i+j] !== needle[j]) {
               break;
            } else if (j === needle.length - 1) {
                return i;
            }
       
        }

    }
    return -1
};