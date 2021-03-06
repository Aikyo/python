"""
Given an array nums of n integers, are there elements
a, b, c in nums such that a + b + c = 0? Find all unique
triplets in the array which gives the sum of zero.

"""
def threeSum(self, nums):
    res = []
    nums.sort()
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l +=1
            elif s > 0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1; r -= 1
    return res
# a = [1,23,4]
# b = a[0-1]
# print(b)
# import numpy as np
# c = np.array(a)
# print(c[0-1])
# print(a)
a = [x for x in enumerate(range(18))]
print(a)


def three_(num):
    num.sort()
    result = []
    for i in range(len(num) - 2):
        if num[i] == num[i-1]:
            continue
        l,r =i+1,len(num) -1
        while l < r:
            s = num[i] + num[l] + num[r]
            if s <0:
                l += 1
            elif s >0:
                r -= 1
            else:
                result.append((num[i],num[l],num[r]))
                while l <r and num[l] == num[l+1]:
                    l+=1
                while l<r and num[r] == num[r-1]:
                    r -=1

                l +=1
                r -= 1
    return result
print("hello i am kiko")
print(three_([-9,-6,-2,-1,1,3,4,2,5]))




