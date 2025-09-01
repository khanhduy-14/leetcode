struct SegTree {
    vector <int> tree;
    SegTree(int n) {
        tree.resize(n*4);
    }

    void build(vector <int> arr, int n, int s, int e) {
        if (s == e) {
            tree[n] = arr[s];
            return;
        }
        int m = (s + e)  / 2;
        build(arr, n * 2, s, m);
        build(arr, n * 2 + 1, m + 1, e);
        tree[n] = max(tree[n*2],tree[n*2+1]);
    }

    int query(int val) {
        if (tree[1] < val) {
            return -1;
        }
        return 1;
    }

    void update(int n, int s, int e, int v) {
        if (s == e) {
            tree[n] = 0;
            return;
        }

        int m = (s + e) / 2;
        int l = n * 2;
        int r= l+1;
        if (tree[l] >= v) {
            update(l, s, m, v);
        }
        else {
            update(r, m+1, e, v);
        }

        tree[n] = max(tree[l],tree[r]);

    }
};

class Solution {
public:
    int numOfUnplacedFruits(vector<int>& fruits, vector<int>& baskets) {
        int n = baskets.size();
        SegTree tree(n);
        tree.build(baskets, 1, 0, n - 1);
        int ans = 0;
        for (int f: fruits) {
            if (tree.query(f) == -1) {
                ans+=1;
            }
            else {
                tree.update(1, 0, n-1, f);
            }
        }
        return ans;

    }
};