class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap={}
        count = 0 
        maxCount = 0
        for n in nums:
            if n in hashMap: 
                return True 

            hashMap[n] = 1 + hashMap.get(n,0)
        return False