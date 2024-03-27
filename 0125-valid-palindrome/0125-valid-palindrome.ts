function isPalindrome(s: string): boolean {
    let l: number = 0, r: number = s.length - 1
    while ( l <= r) {
        const s1 = s.charCodeAt(l);
        const s2 = s.charCodeAt(r);
        
        if(!isLetter(s1)){
            l++
            continue;
        }
        
        if(!isLetter(s2)){
            r--
            continue;
        }
        if(toLowerCase(s1) !== toLowerCase(s2))
        {
            return false;
        }
        l++;
        r--;
    }
    return true
};

function isLetter(code): boolean {
    const isLowerCaseLetter = code >= 97 && code <= 122;
    const isUppercaseLetter = code >= 65 && code <= 90;
    const isNumberLetter = code >= 48 && code <= 57;
    if (isLowerCaseLetter || isUppercaseLetter || isNumberLetter) {
        return true;
    }
    return false;
}

function toLowerCase(code): number  {
    if (code >= 65 && code <= 90) {
        return code + 32;
    }
    else {
        return code;
    }
}