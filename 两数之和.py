from typing import List

# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for lindex,val in enumerate(nums):
            other_val = target - val
            print("target_val " + str(target))
            print("current_val " + str(val) )
            print("other_val "+ str(other_val))
            res = []
            # print("other_val in nums index " + str(nums.index(ot_target)))
            if other_val in  nums and nums.index(other_val) != lindex :
                print("======find other val in list =======" + str(nums.index(other_val)))
                res.append(lindex)
                res.append(nums.index(other_val))
                print("res: "+ str(res))
                break
            print("\n")
        return res




# if __name__ == "__main__":
#     # nums = [2, 7, 11, 15]
#     # nums = [3, 3, 4]
#     # nums = [2, 4, 11, 3]
#     nums = [2, 7, 11, 15]
#     # nums = [3,2,4]
#     target = 9
#     # target = 9
#     so = Solution()
#     res = so.twoSum(nums=nums,target=target)
#     print(res)
