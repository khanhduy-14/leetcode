class Solution {
public:
    double soupServings(int n) {
        if (n > 4800) {
            return 1;
        }

        map<pair<int,int>, double>  m;

        auto solve = [&](auto& self, int a, int b) -> double {
            if (m.count({a,b})) {
                return m[{a,b}];
            }
            if (a <=0 and b <=0) {
                return 0.5;
            }
            if (a<=0) {
                return 1;
            }
            if (b<=0) {
                return 0;
            }

            double res = 0.25 * (
                self(self, a - 100, b) +
                self(self, a - 75, b - 25) +
                self(self, a - 50, b - 50) +
                self(self, a - 25, b - 75) 
            );
            m[{a,b}] = res;
            return res;
        };
        return solve(solve, n,n);
    }
};