/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* modifiedList(vector<int>& nums, ListNode* head) {
        set<int> s(nums.begin(), nums.end());
        while (s.count(head->val)) {
            head = head->next;
        }
        ListNode *prev = head, *curr = head->next;

        while(curr != nullptr) {
            if(s.count(curr->val)) {
                prev->next = curr->next;
            }
            else {
                prev = curr;
            }
            curr = curr->next;
        }
        return head;

    }
};