/**
 Do not return anything, modify matrix in-place instead.
 */
function setZeroes(matrix: number[][]): void {
    let firstRowZeroes: boolean = false;
    
    const row: number = matrix.length;
    const column: number = matrix[0].length;

    for (let r = 0; r < row; r++) {
        for (let c = 0; c < column; c++) {
            const cell = matrix[r][c];
            if (cell === 0) {
                if (r <= 0) {
                    firstRowZeroes = true;
                }
                else {
                    matrix[0][c] = 0;
                    matrix[r][0] = 0;
                }
            }
        }
    }
 
   for (let r = 1; r < row; r++) {
        for (let c = 1; c < column; c++) {
             
            if (matrix[r][0] === 0 || matrix[0][c] === 0) {
                matrix[r][c] = 0;
            }
        }
    }
   if (matrix[0][0] === 0) {
       for (let r = 0; r < row; r++) {
                matrix[r][0] = 0;
        }
   }
                                           
   if (firstRowZeroes) {
        for (let c = 0; c < column; c++) {
                matrix[0][c] = 0;
        }
        
   }

   
       
};