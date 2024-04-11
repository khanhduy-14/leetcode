function generateParenthesis(n: number): string[] {
    const result = [];
    const generate = (stack: string[], text: string, parenthesis: string) => {
        const newStack = [...stack];
        if(parenthesis === ")") {
            if(newStack[newStack.length - 1] === "(") {
                newStack.pop()
            }
            else {
                 newStack.push(parenthesis)
            }
            
        }
        else {
                 newStack.push(parenthesis)
        }
 
        
        
       
        
        text+=parenthesis
        
        if(text.length >= n * 2){
            if(newStack.length === 0){
              result.push(text)
            }
            return;
        }
    
        generate(newStack, text, "(")
        generate(newStack, text, ")")
    }
    
    generate(["("], "(","(")
    generate(["("], "(",")")

   return result
    
};