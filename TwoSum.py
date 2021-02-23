# Dictionary Hasmap
# hashmap = {}
# hashmap[6] = 1
# hashmap[5] = 2
# print("Printing Hasmap %s" %hashmap)

# TwoSum Problem 

# class Solution:
#     def TwoSum(self,nums,target):
#      dict = {}
#      for i in range(0,len(nums)):
#          value = target-nums[i]
#          if(value in dict):
#            return (dict[value],i)
#          else:
#              dict[nums[i]] = i


class Solution:
  def TwoSum(self,nums,target):
    dict = {}
    i = 0
    while i < len(nums):
      value = target - nums[i]
      if value in dict:
        return (dict[value],i)
      else:
        dict[nums[i]] = i
        i+=1


l = Solution()
print(l.TwoSum([5,6,7,9,6,2,74,87,98,56,45,12,35],7))
