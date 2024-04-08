function evalRPN(tokens: string[]): number {
    const stack: string[] = [];
    for (let token of tokens) {
        if(isNaN(Number(token))) {
            const num1 = Number(stack.pop());
            const num2 = Number(stack.pop());
            const result = calculate(num2, num1, token);
            stack.push(String(result));
        }
        else {
            stack.push(String(token));
        }
    }
    return Number(stack[0])
};


function calculate(number1: number, number2: number, operator: string) : number {
    switch (operator) {
        case '+':
            return number1 + number2;
        case '-':
            return number1 - number2;
        case '*':
            return number1 * number2;
        case '/':
            return Math.trunc(number1 / number2);
        default:
            return -1;
    }
}
