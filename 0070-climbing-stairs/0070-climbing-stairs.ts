function climbStairs(n: number): number {
    
    if (n <= 2) return n;
    
    let prevSteps = 1;
    let steps = 2;
    
    for (let i = 3; i < n; i++) {
        steps+=prevSteps;
        prevSteps=steps-prevSteps
    }
    
    return prevSteps + steps;
    
    
};

