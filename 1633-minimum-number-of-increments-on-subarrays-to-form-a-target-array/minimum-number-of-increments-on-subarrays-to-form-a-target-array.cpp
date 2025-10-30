class SegmentTree {
private:
    vector<int> tree;    
    vector<int> arr;
    int n;

    int left(int node) { return node * 2; }
    int right(int node) { return node * 2 + 1; }

    void build(int node, int start, int end) {
        if (start == end) {
            tree[node] = start;
        } else {
            int mid = (start + end) / 2;
            build(left(node), start, mid);
            build(right(node), mid + 1, end);

            int l = tree[left(node)];
            int r = tree[right(node)];

            
            tree[node] = (arr[l] <= arr[r]) ? l : r;
        }
    }

    int query(int node, int start, int end, int L, int R) {
        if (R < start || end < L)
            return -1;
        if (L <= start && end <= R)
            return tree[node];

        int mid = (start + end) / 2;
        int leftIdx = query(left(node), start, mid, L, R);
        int rightIdx = query(right(node), mid + 1, end, L, R);

        if (leftIdx == -1) return rightIdx;
        if (rightIdx == -1) return leftIdx;

        return (arr[leftIdx] <= arr[rightIdx]) ? leftIdx : rightIdx;
    }

public:
    SegmentTree(const vector<int>& input) {
        arr = input;
        n = arr.size();
        tree.assign(4 * n, -1);
        build(1, 0, n - 1);
    }

    int queryMinIndex(int L, int R) {
        return query(1, 0, n - 1, L, R);
    }
};

class Solution {
public:
    int minNumberOperations(vector<int>& target) {
    
        SegmentTree st(target);


        return dfs(st, target, 0, 0, target.size() - 1);;
    }
private:
    int dfs(SegmentTree& st, vector<int>& target, int previous, int left, int right) {
        if (left > right) return 0; 

        int minIdx = st.queryMinIndex(left, right);
        int minVal = target[minIdx];

    
        int extraStep = minVal - previous;

        int leftRes = dfs(st, target, minVal, left, minIdx - 1);
        int rightRes = dfs(st, target, minVal, minIdx + 1, right);

        return extraStep + leftRes + rightRes;
    }
};