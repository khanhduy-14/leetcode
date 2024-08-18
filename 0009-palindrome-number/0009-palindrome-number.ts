function isPalindrome(x: number): boolean {
            if(x < 0){
            return false;
        }
        const str: string = String(x);
        const stack = [];
        
        for(let i = 0; i < str.length; i++) {
            if(i === Math.floor(str.length / 2) && str.length % 2 !== 0) {
                continue;
            }
            if(i < Math.floor(str.length / 2)){
                
                stack.push(str[i])
            }
            else {
                if(stack[stack.length - 1] === str[i]) {
                  stack.pop()
                }
            }
        }
        return stack.length === 0
};