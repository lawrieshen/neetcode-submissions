class Solution {
public:
    bool isValid(string s) {
        std::unordered_map<char, char> reference = {
            {')', '('},
            {']', '['},
            {'}', '{'}
        };

        std::stack<char> stack;

        for (char c : s) {
            if (reference.count(c)) {
                if (stack.empty() || stack.top() != reference[c]) {
                    return false;
                }
                stack.pop();
            } else {
                stack.push(c);
            }
        } 
        
        return stack.empty();
    }
};
