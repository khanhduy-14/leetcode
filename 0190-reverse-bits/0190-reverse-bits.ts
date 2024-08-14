function reverseBits(n: number): number {
    
    
    const convertToBinary = (n: number): string => {
         let str = ""
        while(n !== 0 ){
            str = n%2 + str;
            n = (n - (n % 2)) / 2;
        }
        return str;
    }
    const convertToInteger = (n: string): number => {
        let integer = 0;
        for(let i = 0; i<n.length; i++) {
            integer*=2;
            integer+=Number(n[i]);
        }
        return integer;
    }
    const reverseNumber = (n: string) => {
        let str = ""
        for (let i = n.length - 1; i >=0; i--) {
            str = str + n[i];
        }
        return str;
    }
    let reverseBit = convertToBinary(n);
    while (reverseBit.length < 32) {
        reverseBit = "0" + reverseBit;
    }
  
    
    return convertToInteger(reverseNumber(reverseBit))
	
};