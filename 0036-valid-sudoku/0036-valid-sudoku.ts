function isValidSudoku(board: string[][]): boolean {
    const mapRowNumber = {
        0: {},
        1: {},
        2: {},
        3: {},
        4: {},
        5: {},
        6: {},
        7: {},
        8: {},
        9: {},
    };
    const mapColumnNumber = {
        0: {},
        1: {},
        2: {},
        3: {},
        4: {},
        5: {},
        6: {},
        7: {},
        8: {},
        9: {},
    }
       const mapCellNumber = {
        '00': {},
        '01': {},
        '02': {},
        '10': {},
        '11': {},
        '12': {},
        '20': {},
        '21': {},
        '22': {},
    }
       
       for(let i = 0; i<board.length; i++) {
            for(let j = 0; j<board[i].length; j++) {
                if(board[i][j] === '.') {
                    continue;
                }
                if (mapRowNumber[i][board[i][j]]) {
                    
                    console.log(mapRowNumber[i][board[i][j]])
                    return false;
                }
                else {
                    mapRowNumber[i][board[i][j]] = true;
                }
             if (mapColumnNumber[j][board[i][j]]) {
                 
                    return false;
                }
                else {
                    mapColumnNumber[j][board[i][j]] = true;
                }
             
            if (mapCellNumber[`${Math.floor(i/3)}${Math.floor(j/3)}`][board[i][j]]) {
                
                    return false;
                }
                else {
                    mapCellNumber[`${Math.floor(i/3)}${Math.floor(j/3)}`][board[i][j]] = true;
                }
       }
       }

    return true
};