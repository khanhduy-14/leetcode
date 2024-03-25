function lengthOfLastWord(s: string): number {
    let lengthLastWorld = 0;
    let supportLengthLastWorld=0;
    for(let i=0; i<s.length; i++) {
        if(s[i]!==" "){
            supportLengthLastWorld++;
            lengthLastWorld = supportLengthLastWorld;
        }
        else {
            supportLengthLastWorld=0;
            
        }
    }
    return lengthLastWorld
};