class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_len = 0
        l = 0
        window  = set()
        lst = list(s)

        for r in range(len(lst)):

                while lst[r] in window:
                    window.remove(lst[l])
                    l += 1   

                window.add(lst[r])
                max_len = max(max_len,r - l + 1)    

        return max_len        

        