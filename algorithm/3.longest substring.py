def lengthOfLongestSubstring(s):
    start = maxLength = 0
    usedChar = {}

    for i in range(len(s)):
        if s[i] in usedChar and start <= usedChar[s[i]]:
            start = usedChar[s[i]] + 1
        else:
            maxLength = max(maxLength, i - start + 1)

        usedChar[s[i]] = i

    return maxLength

king = ['feifei',"仲达",'子龙']
a = dict(enumerate(king))
print(a)




















def longestsubstr(strings):
    usedchar={}
    start,ml = 0,0
    for i in range(len(strings)):
        if strings[i] in usedchar and start <= usedchar[strings[i]]:
            start = usedchar[strings[i]] + 1
        else:
            ml = max(ml,i-start + 1)
        usedchar[strings[i]] = i
    return ml
print(longestsubstr("abacasdff"))











