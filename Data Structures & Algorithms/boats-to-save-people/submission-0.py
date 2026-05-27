class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # step 1: find the maximum weight in the array
        m = max(people)
        # step 2: create a count array of size (max + 1) and count the frequency of each weight
        count = [0] * (m + 1)
        for p in people:
                    count[p] += 1
        # step 3: reconstruct the sorted array by iterating thru the count array
        idx, i = 0, 1
        while idx < len(people):
            while count[i] == 0:
                i += 1
            people[idx] = i
            idx += 1
            count[i] -= 1
        # step 4: apply two pointer approach
        res = 0
        l, r = 0 , len(people) - 1
        while l <= r:
            # the heaviest person takes a boat
            remain = limit - people[r]
            r -= 1
            res += 1
            # if the lightest person fits with them, include them too
            if l <= r and people[l] <= remain:
                l += 1

        # step 5: return the result
        return res