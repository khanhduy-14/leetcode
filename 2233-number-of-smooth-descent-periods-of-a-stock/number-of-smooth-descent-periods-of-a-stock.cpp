class Solution {
public:
    long long getDescentPeriods(vector<int>& prices) {
        int n = prices.size();
        long long res = 0, currDesc = 0;
        for (int i = 1; i < n; i++) {
            if(prices[i] +1 == prices[i-1]) {
                currDesc+=1;
            } else if (currDesc>0) {
                currDesc+=1;
                res+= (currDesc * (currDesc + 1)) / 2 - currDesc;
                currDesc = 0;
            }   

        }
        currDesc+=1;
        res+= (currDesc * (currDesc + 1)) / 2 - currDesc;
        res+=n;
        return res;
    }
};