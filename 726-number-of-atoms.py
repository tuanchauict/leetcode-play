# https://leetcode.com/problems/number-of-atoms/description/

class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """

        def count(f, begin):

            index = begin
            result = {}

            while index < len(f):
                c = f[index]
                print index, c
                if c == '(':
                    index, m = count(f, index + 1)
                    print '+', index, m
                    if index < len(f) and f[index].isdigit():
                        num = int(f[index])
                        print '>>', num, m
                        for k, v in m.items():
                            m[k] = v * num
                        index += 1
                    print '-', index
                    print 'm', m, result

                    for k, v in m.items():
                        print '->', k, v
                        result[k] = result.setdefault(k, 0) + v
                elif c == ')':
                    index += 1
                    break
                    # return index, result
                elif c.isdigit():
                    result[f[index - 1]] = int(c)
                else:
                    result[c] = 1
                index += 1
                # print result

            return index, result

        arr = []
        unit = ''
        for c in formula:
            if 'A' <= c <= 'Z':
                if unit:
                    arr.append(unit)
                unit = c
            elif 'a' <= c <= 'z':
                unit += c
            elif '0' <= c <= '9':
                if unit and unit[0] > '9':
                    arr.append(unit)
                    unit = ''
                unit += c
            elif c == '(' or c == ')':
                if unit:
                    arr.append(unit)
                arr.append(c)
                unit = ''
        if unit:
            arr.append(unit)
        print(arr)

        _, result = count(arr, 0)
        print 'result', result


s = Solution()
# s.countOfAtoms("K4(ON(SO3)2)2")
# s.countOfAtoms("(ON(SO3)2)2")
s.countOfAtoms("(O(O3)2)2")
# s.countOfAtoms("Mg(OH)20")
