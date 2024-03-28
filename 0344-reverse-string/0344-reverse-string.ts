/**
 Do not return anything, modify s in-place instead.
 */
function reverseString(s: string[]): void {
    let temp = '';
    for(let i = 0; i < s.length / 2; i++) {
       temp = s[i]
       s[i] = s[s.length - 1 - i]
       s[s.length - 1 - i] = temp
    }  
};