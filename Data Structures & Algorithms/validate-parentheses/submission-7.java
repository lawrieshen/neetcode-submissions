class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> reference = new HashMap<>();
        reference.put(')', '(');
        reference.put('}', '{');
        reference.put(']', '[');

        Deque<Character> stack = new ArrayDeque<>();

        for (char c : s.toCharArray()) {
            if (reference.containsKey(c)) {
                if (stack.isEmpty() || stack.pop() != reference.get(c)) {
                    return false;
                }
            } else {
                stack.push(c);
            }
        }

        return stack.isEmpty();
    }
}
