function letterCombinations(digits: string): string[] {
   const digitToChar: Record<string, string> ={
       "2": 'abc',
       "3": 'def',
       "4": "ghi",
       "5": "jkl",
       "6": "mno",
        "7": 'pqrs',
       "8": 'tuv',
       "9": 'wxzy',
   }
   const res: string[] = [];
       
const backtrack = (i: number, curStr: string) => {
        console.log(curStr)
    if(curStr.length === digits.length ){
        res.push(curStr)
        return;
    }
    for(const c of digitToChar[digits[i]]) {
        backtrack(i+1, curStr + c)
    }
}
    if(digits) {
        backtrack(0, "");
    }
       
    return res

};
    
