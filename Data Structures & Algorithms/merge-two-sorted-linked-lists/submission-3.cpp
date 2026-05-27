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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* dummy = new ListNode();
        ListNode* current = dummy;

        while (list1 != nullptr && list2 != nullptr) {
            int val1 = list1->val;
            int val2 = list2->val;

            if (val1 <= val2) {
                current->next = list1;
                list1 = list1->next;
            } else {
                current->next = list2;
                list2 = list2->next;
            }

            current = current->next;
        }

        while (list1 != nullptr) {
            current->next = list1;
            list1 = list1->next;
            current = current->next;
        }

        while (list2 != nullptr) {
            current->next = list2;
            list2 = list2->next;
            current = current->next;
        }

        return dummy->next;
    }
};
