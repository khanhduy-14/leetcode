function combinationSum(candidates: number[], target: number): number[][] {
    
    const res: Array<number[]> = [];
    
    const backtrack = (i: number, curArr: number[], total: number) => {
      if (total === target) {
          res.push([...curArr]);
          return;
      }
      
      if (i > candidates.length - 1 || total > target) {
          return
      }
      
      curArr.push(candidates[i]);
      backtrack(i, curArr, total + candidates[i]);
      curArr.pop();
      backtrack(i + 1, curArr, total)
    }
    
        backtrack(0, [], 0);
    return res
};