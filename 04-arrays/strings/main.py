from typing import List


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Own find method
        """
        n = len(haystack)

        for i in range(n):
            if haystack[i] == needle[0]:
                # print("match", i, haystack[i])
                f_index = i
                m = 1
                left = i + 1
                right = 1

                # print(haystack[/left], needle[right])
                while left < n and right < len(needle):
                    if haystack[left] == needle[right]:
                        m += 1
                    else:
                        break

                    left += 1
                    right += 1

                if m == len(needle):
                    return f_index

        return -1

    def reverse_words(self, s: str) -> str:
        """
        TC -> O(n) (O(n) + O(n) + O(n))
        SC -> O(n) ( O(n) + O(n))
        """
        ans = ""
        n = len(s)

        i = 0
        stack = []
        while i < n:
            if s[i] == " ":
                i += 1
                continue

            # temp = i
            temp_str = ""
            while i < n and s[i] != " ":
                temp_str += s[i]
                i += 1
            print(temp_str)

            stack.append(temp_str)

        for i in range(len(stack) - 1, -1, -1):
            if i == 0:
                ans += stack[i]
            else:
                ans += stack[i] + " "
        return ans

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for i in range(len(strs)):
            if i == len(strs) - 1:
                ans += strs[i]
            else:
                ans += strs[i] + "::;"

        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        # neet::;code::;love::;you::;
        temp = ""
        i = 0
        n = len(s)

        while i < n:
            if s[i] == ":" and s[i + 1] == ":" and s[i + 2] == ";":
                print("got", temp)
                ans.append(temp)
                temp = ""
                i += 2
            else:
                temp += s[i]
                # print(s[i])

            i += 1
        ans.append(s[i - 3 : n])
        return ans

    def reverse_vowels(self, s: str) -> str:
        ans = list(s)
        i, j = 0, len(s) - 1
        vl = set("aeiouAEIOU")
        while i <= j:
            # left = s[i].lower()
            while i <= j and s[i] not in vl:
                i += 1
            # right = s[j].lower()
            while i <= j and s[j] not in vl:
                j -= 1
            if i > j:
                break
            ans[i], ans[j] = ans[j], ans[i]
            print(ans)
            i += 1
            j -= 1

        return "".join(ans)

    def removeOccurrences(self, s: str, part: str) -> str:
        """
        ans = ""
        s = list(s)
        n = len(s)
        n2 = len(part)
        i = 0


        while i < n:
            if s[i] is None:
                continue
            # Matched first word
            if s[i] == part[0]:
                # Check for other words also
                temp = str(s[i])
                m = i + 1

                for j in range(1, n2):
                    if m < n and s[m] == part[j] and s[m] is not None:
                        temp += str(s[m])
                    else:
                        break
                    m += 1

                if temp == part:
                    for l in range(i, m):
                        s[l] = None

                    i = m

                print(temp)

            i += 1

        """
        n2 = len(part)
        ans = []
        for ch in s:
            ans.append(ch)

            if ch == part[-1]:
                print(ans, ans[-n2:], part)
                if part == "".join(ans[-n2:]):
                    del ans[-n2:]
                    print("answer ", ans)

        print(ans)
        return "".join(ans)


x = Solution()
a = x.removeOccurrences("daabcbaabcbc", "abc")
print(x.removeOccurrences("axxxxyyyyb", "xy"))
# print(a)
# print(a)

# print(x.reverse_words("  hello world  "))
# print(x.reverse_words("a good   example"))
