import heapq
class Solution:
    def furthestBuilding(self,heights,bricks,ladders):
        heap = []
        for i in range(1,len(heights)):
            diff = heights[i]-heights[i-1]
            if(diff > 0):
                heapq.heappush(heap,diff)
            if(len(heap)<=ladders):
                continue
            bricks -= heapq.heappop(heap)
            if (bricks<0):
                return i-1
        return len(heights)-1


l = Solution()
ans = l.furthestBuilding([4,2,7,6,9,14,12],5,1)
print(ans)
# [4,2,7,6,9,14,12]
# 5
# 1
# expected 4 