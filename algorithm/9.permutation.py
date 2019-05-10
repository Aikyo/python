"""
Given a collection of distinct integers, return all possible permutations.

the basic idea is, to permute n numbers, we can add the nth number into the
resulting List<List<Integer>> from the n-1 numbers, in every possible position.

For example, if the input num[] is {1,2,3}: First, add 1 into the initial
List<List<Integer>> (let's call it "answer").

Then, 2 can be added in front or after 1. So we have to copy the List in
answer (it's just {1}), add 2 in position 0 of {1}, then copy the original
{1} again, and add 2 in position 1. Now we have an answer of {{2,1},{1,2}}.
There are 2 lists in the current answer.

Then we have to add 3. first copy {2,1} and {1,2}, add 3 in position 0; then
copy {2,1} and {1,2}, and add 3 into position 1, then do the same thing for
position 3. Finally we have 2*3=6 lists in answer, which is what we want.
"""

def permute(nums):
    perms = [[]]
    for n in nums:
        new_perms = []
        for perm in perms:
            for i in range(len(perm)+1):
                new_perms.append(perm[:i] + [n] + perm[i:])   ###insert n
        perms = new_perms
    return perms

print(permute([1,2,3]))


a = [1,2,3,4,5,6,7]
b = [8,9]
print(a+b)
a.extend(b)
print(a)
#在list的第n个位置插入 key

def insert_(num,n,key):
    return num[:n] + [key] + num[n:]

print(insert_(a,2,33))





def permutation(num):
    res = [[]]
    for n in num:
        pre = []
        for r in res:
            for i in range(len(r) +1):
                pre.append(r[:i] + [n] + r[i:])
        res = pre
    return res

print(permutation([3,4,5]))















