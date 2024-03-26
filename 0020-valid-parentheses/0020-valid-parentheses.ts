function isValid(s: string): boolean {
     const stack = [];
     const map  = {
        '{' : '}',
        '(' : ')',
        '[' : ']',
    }
    for(let i=0; i<s.length ; i++) {
 
         if(map[stack[stack.length - 1]] === s[i]) {
      
            stack.pop();
        }
        else {
            stack.push(s[i])
        }
    }
   
    return stack.length === 0;
};