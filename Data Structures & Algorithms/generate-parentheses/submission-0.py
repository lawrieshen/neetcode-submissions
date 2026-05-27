class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current, open_count, close_count):

            # base case
            if len(current) == 2 * n:
                result.append(current)
                return

            # add open paranthese if we haven't
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)
            
            if open_count > close_count:
                backtrack(current + ")", open_count, close_count + 1)

        
        backtrack("", 0, 0)

        return result