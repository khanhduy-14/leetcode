class Solution {
public:
    int countValidSelections(vector<int>& nums) {
       int sum=0, curr=0, res=0;
       for (int num: nums){
        sum+=num;
       } 
        for (int num: nums){
            curr+= num;
            if (num == 0) {
                if (curr * 2 == sum) {
                    res+=2; 
                }
                if (abs(curr*2 - sum) == 1) {
                    res+=1;
                }
                
            }
       }
       return res;
    }
};