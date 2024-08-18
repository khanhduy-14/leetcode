function isPalindrome(x: number): boolean {
    let reverse = 0
    let copy = x;
    
    while(copy > 0) {
        reverse = reverse * 10 + copy % 10;
        copy = Math.floor(copy/10);
    }

    return x === reverse
};