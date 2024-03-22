class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            j = target - i
            if j in nums:
                if i == j:
                    try:
                        return [nums.index(i),nums.index(j,(nums.index(i)+1))]
                    except:
                        pass
                else:
                    return [nums.index(i),nums.index(j)]
