class MinStack {
    stack: Array<Record<string, number>>;
    constructor() {
        this.stack = new Array();
    }

    push(val: number): void {
        this.stack.push({
            value: val,
            min: this.stack.length === 0 ? val : Math.min(this.getMin(), val),
        });
    }

    pop(): void {
       this.stack.pop();
    }

    top(): number {
       return this.stack[this.stack.length - 1].value;
    }

    getMin(): number {
        return this.stack[this.stack.length - 1].min;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */