class Solution {
public:
    long long getDescentPeriods(vector<int>& prices) {
        int n = prices.size();
        long long res = 0, currDesc= 0;
        for (int i = 0; i < n; i++) {
            if(i > 0 && prices[i] +1 == prices[i-1]) {
              currDesc+=1;
            } else {
              currDesc=1;
            } 
            res+= currDesc;

        }
        return res;
    }
};