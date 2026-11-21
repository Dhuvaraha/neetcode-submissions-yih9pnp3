class Solution:
    def hasDuplicate(self, nums):
       seen = set()
       #duplicate = False
       for x in nums:
            if x in seen:
                return True
            seen.add(x)
       return False    