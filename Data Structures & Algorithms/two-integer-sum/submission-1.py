class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable={}
        for i in range(len(nums)):
            hashtable[nums[i]]=i
        firstind=0
        secondind=0
        for i  in range(len(nums)):
            firstind=i
            reqval=target-nums[i]

            if reqval in hashtable:
                if firstind!=hashtable[reqval]:
                    secondind=hashtable[reqval]
                    break

        return [firstind,secondind]

        