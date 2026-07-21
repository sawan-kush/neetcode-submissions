class Solution:
    def minWindow(self, s: str, t: str) -> str:

        from collections import Counter

        if len(t) > len(s):
            return ""

        target = Counter(t)
        window = {}
        min_len = float("inf")

        left = 0
        have = 0
        need = len(target)
        res = [-1,-1]

        for right in range(len(s)):

            char = s[right]

            window[char] = window.get(char,0) + 1

            if char in target and window[char] == target[char]:
                have += 1

                while have == need:

                    resLen = right - left + 1
                    if resLen < min_len:
                        res = [left,right]
                        min_len = resLen
      
                    window[s[left]] -= 1
                    if s[left] in target and window[s[left]] < target[s[left]]:
                        have -= 1

                    left += 1    

        left,right = res
        return s[left:right + 1] if min_len != float("inf") else ""




                        



        