function isPalindrome(s: string): boolean {
    const str: string = s.toLowerCase().replace(/[^0-9a-zA-Z]/g, '')
    let l: number = 0, r: number = str.length - 1
    while ( l <= r) {
        if(str[l]!==str[r]){
            return false
        }
        l++;
        r--;
    }
    return true
};