class Solution {
public:
    bool isValidCode(const string& s) {
            if (s == "") {
                return false;
            }
            for (char c : s) {
                if (!isalnum(c) && c != '_') {
                    return false;
                }
            }
            return true;
    }

    int getOrderByCat(const string& c) {
        if (c == "electronics") return 0;
        if (c == "grocery")     return 1;
        if (c == "pharmacy")    return 2;
        if (c == "restaurant")  return 3;
        return -1;
    }

    vector<string> validateCoupons(vector<string>& code, vector<string>& businessLine, vector<bool>& isActive) {
         vector<pair<int, string>> validArr;
         for (int i = 0; i < code.size(); i++) {
            if (!isActive[i]) continue;

            if (!isValidCode(code[i])) continue;

            
            int order = getOrderByCat(businessLine[i]);
            if (order == -1) continue;


            validArr.push_back({order, code[i]});
        }

        sort(validArr.begin(), validArr.end());

        vector<string> res;

        for (auto& p : validArr) {
            res.push_back(p.second);
        }

        return res;

    }
};