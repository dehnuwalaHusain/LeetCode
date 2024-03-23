class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestLength = 0
        firstIndex = 0
        longestSubstring = ""
        i = 0
        while i < len(s):
            if s[i] not in longestSubstring:
                if longestSubstring == "":
                    firstIndex = i
                longestSubstring += s[i]
                i += 1
            else:
                longestSubstring = ""
                if i != len(s):
                    i = firstIndex + 1
                #print("first index - ", firstIndex, " i - ", i)
            length = len(longestSubstring)
            if length > longestLength:
                longestLength = length
        return longestLength