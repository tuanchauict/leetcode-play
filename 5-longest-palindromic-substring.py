from utils import evaluate


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        m = {}

        for i, c in enumerate(s):
            m.setdefault(c, []).append(i)

        mm = {}

        for c, a in m.items():
            mm[c] = []

        print(m)

        return ''

    def bf(self, s):
        l = len(s)
        mi = 0
        res = ''
        for i in range(l):
            # print(mi)
            for j in range(mi, (l - i) // 2 + 1):
                s0 = s[i:i + j + 1]
                s1 = s[i + j + j + 1:i + j:-1]
                s2 = s[i + j + j + 2:i + j + 1:-1]
                h0 = hash(s0)
                h1 = hash(s1)
                h2 = hash(s2)
                # print(s[i:i+j+1] , s[i:i+j+1] , s[i+j+j+2:i+j+1:-1])
                if h0 == h1 and len(s[i:i + j + j + 2]) > len(res):
                    res = s[i:i + j + j + 2]
                    mi = len(res) // 2 - 1
                    # print(res)
                if h0 == h2 and len(s[i:i + j + j + 3]) > len(res):
                    res = s[i:i + j + j + 3]
                    mi = len(res) // 2 - 1
                    # print(res)
        if not res:
            res = s[0]
        return res

    def bf2(self, s):
        if not s:
            return ''
        l = len(s)
        mi = 0
        offset = 0
        length = 0
        for i in range(l):
            for j in range(mi, min(i, l - i - 1) + 1):
                # print(i, j)
                if s[i - j] == s[i + j]:
                    # print(s[i - j:i + j + 1])
                    if length < 2 * j + 1:
                        offset = i - j
                        length = 2 * j + 1

                    # if j * 2 + 1 > len(res):
                    #     res = s[i - j:i + j + 1]
                else:
                    break

            for j in range(mi, min(i, l - i - 2) + 1):
                # print(i, j)
                if s[i - j] == s[i + j + 1]:
                    if length < 2 * (j + 1):
                        offset = i - j
                        length = 2 * (j + 1)
                else:
                    break

        return s[offset:offset + length]


sol = Solution()
s = "mwwfjysbkebpdjyabcfkgprtxpwvhglddhmvaprcvrnuxifcrjpdgnktvmggmguiiquibmtviwjsqwtchkqgxqwljouunurcdtoeygdqmijdympcamawnlzsxucbpqtuwkjfqnzvvvigifyvymfhtppqamlgjozvebygkxawcbwtouaankxsjrteeijpuzbsfsjwxejtfrancoekxgfyangvzjkdskhssdjvkvdskjtiybqgsmpxmghvvicmjxqtxdowkjhmlnfcpbtwvtmjhnzntxyfxyinmqzivxkwigkondghzmbioelmepgfttczskvqfejfiibxjcuyevvpawybcvvxtxycrfbcnpvkzryrqujqaqhoagdmofgdcbhvlwgwmsmhomknbanvntspvvhvccedzzngdywuccxrnzbtchisdwsrfdqpcwknwqvalczznilujdrlevncdsyuhnpmheukottewtkuzhookcsvctsqwwdvfjxifpfsqxpmpwospndozcdbfhselfdltmpujlnhfzjcgnbgprvopxklmlgrlbldzpnkhvhkybpgtzipzotrgzkdrqntnuaqyaplcybqyvidwcfcuxinchretgvfaepmgilbrtxgqoddzyjmmupkjqcypdpfhpkhitfegickfszermqhkwmffdizeoprmnlzbjcwfnqyvmhtdekmfhqwaftlyydirjnojbrieutjhymfpflsfemkqsoewbojwluqdckmzixwxufrdpqnwvwpbavosnvjqxqbosctttxvsbmqpnolfmapywtpfaotzmyjwnd"
# s = 'abac'
# sol.longestPalindrome(s)

evaluate(sol.bf, s)
evaluate(sol.bf2, s)
