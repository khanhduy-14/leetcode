function generate(numRows: number): number[][] {
    const triangle = Array.from({length: numRows}, (_,i) => Array.from({length: i+1},()=>1))

    for(let i=0; i < triangle.length; i++) {
        
        for(let j=0; j< triangle[i].length;j++) {
            triangle[i][j] = binomialCoeff(i,j)
        }
    }
    return triangle
};

const binomialCoeff = (n, k) => {
    let res = 1

    for (let i = 0; i < k; i++) {
        res *= (n - i)
        res /= (i + 1)
    }
    return res
}