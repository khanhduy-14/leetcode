class Solution {
public:
    long long maxPower(vector<int>& stations, int r, int k) {
        int n = stations.size();

        // --- Tính power hiện tại mỗi city bằng prefix difference ---
        vector<long long> diff(n + 1, 0);
        for (int i = 0; i < n; i++) {
            diff[max(0, i - r)] += stations[i];
            if (i + r + 1 < n)
                diff[i + r + 1] -= stations[i];
        }

        vector<long long> power(n, 0);
        power[0] = diff[0];
        for (int i = 1; i < n; i++)
            power[i] = power[i - 1] + diff[i];

        // --- Binary search trên đáp án ---
        long long low = 0, high = 1e14, ans = 0;
        while (low <= high) {
            long long mid = (low + high) / 2;
            if (can(power, r, k, mid)) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return ans;
    }

private:
    bool can(vector<long long>& power, int r, long long k, long long target) {
        int n = power.size();
        vector<long long> added(n, 0);
        long long windowSum = 0;

        for (int i = 0; i < n; i++) {
            if (i - r - 1 >= 0) windowSum -= added[i - r - 1];
            long long current = power[i] + windowSum;

            if (current < target) {
                long long need = target - current;
                if (need > k) return false;
                k -= need;
                windowSum += need;
                if (i + r < n)
                    added[i + r] += need;
            }
        }
        return true;
    }
};