class Solution:
    def findRadius(self, houses, heaters) -> int:
        
        l = 0
        r = max(abs(houses[0] - heaters[-1]), abs(houses[-1] - heaters[0]))
        def capableToHeat(radius) -> bool:
            i = 0
            j = 0
            while i < len(heaters):
                while j < len(houses):
                    length = abs(heaters[i] - houses[j])
                    if length <= radius:
                        j += 1
                    else:
                        if i == len(heaters) - 1:
                            return length <= radius
                        i += 1
                    if i == len(heaters):
                        return j == len(houses) - 1
                return i < len(heaters)
        

        while l < r:
            mid = (l + r) // 2
            if capableToHeat(mid):
                r = mid
            else:
                l = mid + 1
        return l

trial = Solution()
o = trial.findRadius(houses = [282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923], heaters = [823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612])
print(o)