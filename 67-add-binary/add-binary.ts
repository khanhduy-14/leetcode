function addBinary(a: string, b: string): string {
  let i: number = a.length - 1, j: number =  b.length - 1, result: string[] = [];
  let num =0;
  while(a[i] || b[j]) {
      const num1 = Number(a[i] ?? 0);
      const num2 = Number(b[j] ?? 0);
      
      const sum = num1 + num2 + num;
       num = Math.floor(sum / 2);
      result.unshift((sum % 2).toString());
      i--;
      j--;
      
  }

    if(num > 0) {
        result.unshift(num.toString());
    }
    return result.join('')
  
};