class Solution {
public:
    int minimumBoxes(vector<int>& apple, vector<int>& capacity) {
        sort(capacity.begin(), capacity.end());

        int sum = accumulate(apple.begin(), apple.end(), 0);

        int res = 0, i = capacity.size() - 1;
        
        while(sum > 0) {
            sum -= capacity[i];
            res++;
            i--;
        }

        return res;
    }   
};  