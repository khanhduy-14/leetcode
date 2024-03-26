function romanToInt(s: string): number {
    const mapRomanInteger = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    let i = s.length - 1;
    let sum = 0;
    for (i; i>=0; i--) {
        if(mapRomanInteger[s[i - 1]] < mapRomanInteger[s[i]]) {
            sum+= (mapRomanInteger[s[i]] - mapRomanInteger[s[i - 1]])
            i--;
        }
        else {
            sum+=mapRomanInteger[s[i]]
        }
    }
    return sum;
};