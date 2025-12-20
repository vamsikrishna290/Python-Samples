class Solution:
    @staticmethod
    def length_of_longest_substring(s: str) -> int:
        seen = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            print(f"8: {s[right]} -> {seen}")
            while s[right] in seen:
                # cut the string until you see the repeated char
                # print(f" removing {s[left]}, left={left}, right={right}")
                seen.remove(s[left])
                left += 1
                # print(f"12: {seen}, left: {left}")
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len

if __name__ == '__main__':
    res = Solution().length_of_longest_substring("abcdefghijdef")
    print(res)