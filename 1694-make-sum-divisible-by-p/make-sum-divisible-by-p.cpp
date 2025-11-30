class Solution {
public:
    int arrayMethod(vector<int>& nums, int p, int n, int modP) {
        vector<int> pos(p, INT_MAX);
        pos[0] = -1;

        int len = n, sumP =0;

        for (int i = 0; i<n; i++) {
            sumP=(sumP + nums[i])%p;
            int y = (sumP - modP + p) % p;
            if(pos[y] != INT_MAX) {
                len = min(len, i - pos[y]);
            } 
            pos[sumP] = i;
        }

        return len == n ? -1 : len;
    }

     int unorderedMapMethod(vector<int>& nums, int p, int n, int modP) {
        unordered_map<int,int> hm= {{0, -1}};
        hm.reserve(n);
   

        int len = n, sumP =0;

        for (int i = 0; i<n; i++) {
            sumP=(sumP + nums[i])%p;
            int y = (sumP - modP + p) % p;
            if(hm.count(y)) {
                len = min(len, i - hm[y]);
            } 
            hm[sumP] = i;
        }

        return len == n ? -1 : len;
    }


    int minSubarray(vector<int>& nums, int p) {
        int n = nums.size();
        long long modP = accumulate(nums.begin(), nums.end(), 0LL) % p;
        if(modP==0) return 0;
        return p > n ? unorderedMapMethod(nums,p, n, modP) : arrayMethod(nums,p,n,modP);
    }
};