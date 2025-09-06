class Solution {
public:

    static long long preComputeSum(long long n) {
        if (n<=0) {
            return 0;
        }
        int k=0 ;
        long long ans = 0, p=1;

        while(true) {
            long long np = p* 4;
            if (n>= np) {
                ans+= ((np - p) * (long long)(k+1));
                k+=1;
                p*=4;
            }
            else {
                ans+= ((n-p+1) * (long long)(k+1));
                break;
            }

        }
        return ans;
    }
    long long minOperations(vector<vector<int>>& queries) {
        long long ans = 0;
        for (auto q: queries) {
            ans+= (( preComputeSum(q[1]) - preComputeSum(q[0] - 1) + 1 )  / 2);
        }
        return ans;
    }
};