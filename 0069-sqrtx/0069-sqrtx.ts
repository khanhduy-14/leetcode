function mySqrt(x: number): number {
    if (x === 0) {
        return 0;
    }
    if (x < 4) {
        return 1;
    }
    let i = 2;
    
    while (i * i < x) {
        i+=1
    }
    if (i * i > x) {
        i-=1;
    }
    return i
    
};