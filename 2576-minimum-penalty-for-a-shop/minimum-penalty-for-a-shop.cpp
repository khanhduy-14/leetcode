class Solution {
public:
    int bestClosingTime(string customers) {
        int n = customers.size(), res = 0, penalty = 0;

        for (char c : customers) if (c == 'Y') penalty++;

        int min_penalty = penalty;

        for (int i = 0; i < n; i++) {
             if (customers[i] == 'Y') penalty--; else penalty++;
             cout << penalty << endl;
             if (penalty < min_penalty) {
                min_penalty = penalty;
                res = i + 1;
             }

        }

        return res;
    }
};