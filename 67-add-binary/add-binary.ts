function addBinary(a: string, b: string): string {
  let carry: number = 0, i: number = a.length - 1, j: number = b.length - 1, result = '';
    
  while (i>=0 || j>=0 || carry) {
      let sum = carry;
      
      if(a[i]) sum+= Number(a[i]);
      if(b[j]) sum+= Number(b[j]);
      
      result = (sum % 2) + result;
      carry = Math.floor(sum / 2);
      
      i--;
      j--;
      
  }
    return result
  
};