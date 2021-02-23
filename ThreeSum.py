class Solution:
    def threeSum(self,nums):
        result = []
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            s,e = i+1,n-1
            target = nums[i] * -1
            while s<e:
                if nums[s]+nums[e] == target:
                    result.append[nums[i],nums[s],nums[e]]
                    s+1
                    while s<3 nums[s] == nums[s-1]:
                        s+1
                elif nums[s]+nums[e] < target:
                    s+1
                else:
                    e-1
        return result

l = Solution()
ans = l.threeSum([-1,0,1,2,-1,-4])
print(ans)