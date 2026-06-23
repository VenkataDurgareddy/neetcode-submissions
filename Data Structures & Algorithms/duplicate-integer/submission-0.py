class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited=[]
        for i in range(len(nums)):
            if nums[i] in visited:
                return True
            else:
                visited.append(nums[i])
        print(visited)
        return False