function isHappy(n: number): boolean { 
  let sum = calculateDigitsNumber(n);
  const set = new Set<number>();
  while(!set.has(sum)) {
      set.add(sum)
      sum = calculateDigitsNumber(sum);
  }
  
  if(sum === 1) {
      return true;
  } 
  return false;
};

function calculateDigitsNumber(n: number): number {
    let sum = Math.pow(Number(String(n)[0]),2);
    
    for(let i = 1; i< String(n).length; i++) {
        sum += Math.pow(Number(String(n)[i]),2);
    }
    return sum;
    
}