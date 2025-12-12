using namespace std;

class Solution {
public:
    vector<int> countMentions(int numberOfUsers, vector<vector<string>>& events) {
       sort(events.begin(), events.end(), [](const vector<string> &a, const vector<string> &b){
            long long ta = stoll(a[1]);
            long long tb = stoll(b[1]);
            if (ta != tb) return ta < tb;

            if (a[0] == "OFFLINE" && b[0] == "MESSAGE") return true;
            if (a[0] == "MESSAGE" && b[0] == "OFFLINE") return false;

            return false;
        });
        vector<int> res(numberOfUsers, 0);
        vector<bool> online(numberOfUsers, true);

        priority_queue<pair<long long,int>, 
                       vector<pair<long long,int>>, 
                       greater<pair<long long,int>>> pq;

        for (auto e : events) {
            string type = e[0];
            long long t = stoll(e[1]);

            while (!pq.empty() && pq.top().first <= t) {
                auto [time_online, uid] = pq.top();
                pq.pop();
                online[uid] = true;
            }

            if (type == "OFFLINE") {
                int id = stoi(e[2]);

                if (online[id]) {
                    online[id] = false;
                    pq.push({t + 60, id});
                }
            }

            else {
                string msg = e[2];

                if (msg == "ALL") {
                    for (int i = 0; i < numberOfUsers; i++)
                        res[i]++;
                }
                else if (msg == "HERE") {
                    for (int i = 0; i < numberOfUsers; i++)
                        if (online[i])
                            res[i]++;
                }
                else {
                    for (int i = 0; i < msg.size(); i++) {
                        if (msg[i] == 'i' && msg[i+1] == 'd') {
                            int j = i + 2;
                            while (j < msg.size() && isdigit(msg[j])) j++;
                            int id = stoi(msg.substr(i + 2, j - (i + 2)));
                            res[id]++;
                            i = j;
                        }
                    }
                }
            }
        }

        return res;
    }
};
