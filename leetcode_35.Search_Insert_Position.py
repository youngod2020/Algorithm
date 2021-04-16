# 35. Search Insert Position

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        nums.append(target)
        
        my_set = set(nums) 
        my_list = list(my_set) 
        my_list.sort()
        
        for i in range(len(my_list)):
            if my_list[i] == target:
                
                return i
            
    
        
