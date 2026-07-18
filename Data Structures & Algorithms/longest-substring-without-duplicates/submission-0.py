class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_len = 0
        l = 0
        window  = []
        lst = list(s)

        for r in range(len(lst)):
            if lst[r] not in window:
                window.append(lst[r])
                max_len = max(max_len,r - l + 1)
            else:
                while lst[r] in window:
                    window.remove(lst[l])
                    l += 1    
                window.append(lst[r])
                max_len = max(max_len,r - l + 1)    

        return max_len        

        