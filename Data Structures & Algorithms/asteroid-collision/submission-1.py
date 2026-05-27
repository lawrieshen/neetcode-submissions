class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        j = - 1

        for a in asteroids:
            while j >= 0 and a < 0 and asteroids[j] > 0:
                diff = a + asteroids[j]
                if diff < 0:
                    j -= 1
                elif diff > 0:
                    a = 0
                else:
                    a = 0
                    j -= 1

            if a:
                j += 1
                asteroids[j] = a

        return asteroids[:j + 1]
