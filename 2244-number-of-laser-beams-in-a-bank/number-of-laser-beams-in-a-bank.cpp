class Solution {
public:
    int numberOfBeams(vector<string>& bank) {
        int res = 0, curr = 0;
        for (auto floor_plan : bank) {
            int count = 0;
            for (int i = 0; i < floor_plan.length(); i++) {
                if (floor_plan[i] == '1') {
                    count++;
                }
            }
            if (count > 0) {
                if (curr > 0) {
                    curr*=count;
                    res+=curr;  
                }
                curr=count;
                
            }
        }
        return res;

    }
};