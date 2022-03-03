class Solution: 
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            addAsteroid = True
            while asteroid < 0 and stack and stack[-1] >= 0:
                if stack[-1] >= abs(asteroid):
                    if stack[-1] == abs(asteroid): stack.pop()
                    addAsteroid = False
                    break
                stack.pop()
            if addAsteroid:
                stack.append(asteroid)
        return stack
