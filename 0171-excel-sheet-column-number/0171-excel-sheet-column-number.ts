function titleToNumber(columnTitle: string): number {
    let number = 0;
     for(let i = columnTitle.length - 1; i >= 0; i--) {
       const position = columnTitle.length - 1 - i
       const numberOfChar = columnTitle.charCodeAt(i) - 64
       if (position > 0) {
            number += Math.pow(26, position) * numberOfChar;
       }
         else {
             number += numberOfChar
         }
       
       
     }
    return number
};