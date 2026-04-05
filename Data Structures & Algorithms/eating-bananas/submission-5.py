class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        
        left = 1
        right = max(piles)

        while(left < right):
            mid = (left + right) // 2
            if self.calculateHours(mid, piles) <= h:
                right = mid
            elif self.calculateHours(mid, piles) > h:
                left = mid + 1

        return left
    

    def calculateHours(self, k, piles):
        hours = 0
        for pile in piles:
            full_hour = pile // k
            if pile % k == 0:
                hours += full_hour
            else:
                hours += full_hour + 1

        return hours
