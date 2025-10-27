class Solution {
public:
    int totalMoney(int n) {
        int a = n / 7;
        int b = n % 7;
        return 28*a + 7*(a * (a-1)/2) + ((2*a + b + 1) * b/ 2);
    }
};