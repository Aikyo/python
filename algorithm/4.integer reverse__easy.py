string1 = 'helloiamkiko'
a = string1[::-1]

print(a)


"""
Given a 32-bit signed integer, reverse digits of an integer.
which range  -(2**31) < x < 2**31 -1

2-bit signed integer
00 01 10 11
0  1  -1  -2 
"""
class IntegerInverse:
    def within_range(self, v):
        if v < -(2**31) or v > 2**31 - 1:
            return 0
        else:
            return 1
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not self.within_range(x):
            return 0
        else:
            r = 0
            if x < 0:
               sign = -1
            else:
               sign = 1
            value = sign*x
            while 1:
               r += value % 10
               value = value//10
               if value is 0:
                   break
               r = r*10
            return sign*r*self.within_range(sign*r)
 

util = IntegerInverse()
a = util.reverse(789)
print(a)


def with_32(num):
    if -(2**32) < num < 2**31 -1:
        return 1
    else:
        return 0

if not with_32(2234):
    print("hello herman")
else:
    print("kaishiyunsuan")
if not 0:
    print("hello i am 0")

print(with_32(10))

def reverse_integer(num):
    if not with_32(num):
        return 0
    else:
        if num < 0:
            sign =-1
        else:
            sign = 1
        value = num * sign
        r = 0

        while 1:
            r = r + value % 10
            value = value // 10
            if value is 0:
                break
            r = r * 10
        return r
print("ddd")
print(reverse_integer(1012))
















