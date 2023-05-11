class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        print(f"the string is {s}")
        if len(s) == 0:
            return 0
        if len(s) == 1 or len(s) == 2:
            return len(set(s))
        maxlength = 1
        
        i = 1
        j = i - 1
        while j >= 0 and i < len(s):
            s_len = i+1-j
            if (s[j] not in s[j+1:i+1]) and (s[i] not in s[j:i]):
                
                print(f"{s[j]} not in {s[j+1:i+1]} and {s[i]} not in {s[j:i]}; j round: i={i};j={j};maxlength={maxlength};s_len={s_len}")
                if maxlength <= s_len:
                    maxlength = s_len
                
            elif s[j] in s[j+1:i+1]:
                if j < i - 1:
                    j += 1
                # print(f"{s[j]} in {s[j+1:i+1]} or {s[i]} in {s[j:i]}; j round")

            s_len = i+1-j
            
            if s[i] not in s[j:i]:
                print(f"{s[i]} not in {s[j:i]}; i round: i={i};j={j};maxlength={maxlength};s_len={s_len}")
                if maxlength <= s_len:
                    maxlength = s_len
                i += 1 if i < len(s) else i
            else:

                print(f"{s[i]} in {s[j:i]}; i round")
                j = s[j:i].index(s[i]) + 1 + j
                i += 1
                
        return maxlength


if __name__ == "__main__":
    Solution = Solution()
    print(Solution.lengthOfLongestSubstring("pwwkew"))
    