class Solution {
public:
    int maxProfit(int n, vector<int>& present, vector<int>& future, vector<vector<int>>& hierarchy, int budget) {
        vector<vector<int>> tree(n+1); 
        map<pair<int,int>, vector<int>> dp;
        for (int i = 0; i < n - 1; i++) { 
            tree[hierarchy[i][0]].push_back(hierarchy[i][1]);
        }


        function<vector<int>(int,int)> dfs = [&](int node, int isParentBought) -> vector<int> {
            auto key = make_pair(node, isParentBought);
            if (dp.find(key) != dp.end()) {
                return dp[key];
            }
           
            vector<int> dontBuy(budget+1, 0), buyChildren(budget+1, 0), buy(budget+1, 0), temp(budget+1, 0), take(budget+1,0);
            for (auto v : tree[node]) {
                vector<int> child = dfs(v, 0);
                for (int i = 0; i <= budget; i++) {
                    for (int j = 0; j <= i; j++) {
                        temp[i] = max(temp[i], child[j] + dontBuy[i-j]);
                    }
                }
                dontBuy = temp;
            }
           
            temp.assign(budget + 1, 0);

            int currentNodeCost  = isParentBought == 1 ? present[node-1]/ 2 : present[node-1];
            int currentNodeProfit  = future[node-1] - currentNodeCost ;
            for (auto v : tree[node]) {
                vector<int> child = dfs(v, 1);

                for (int i = 0; i <= (budget - currentNodeCost); i++) {
                    for (int j = 0; j <= i; j++) {
                        temp[i] = max(temp[i], child[j] + buyChildren[i-j]);
                    }
                }
               buyChildren = temp;
            }
            
            for (int i = currentNodeCost; i <= budget; i++) {
                buy[i] = currentNodeProfit + buyChildren[i - currentNodeCost];
            }

            for(int i = 0; i <= budget; i++) {
                take[i] = max({dontBuy[i], buy[i], 0});
            }

            return dp[make_pair(node, isParentBought)] = take;
        };

        vector<int> res = dfs(1,0);
        return *max_element(res.begin(), res.end());;

    }
};