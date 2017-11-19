# https://leetcode.com/problems/number-of-atoms/description/


def create_unit(formula):
    """
    :type formula: str
    :rtype: str
    """
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
    return arr


class Solution(object):
    def sol2(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        units = create_unit(formula)
        stack = []

        for i, s in enumerate(units):
            if s == '(':
                stack.append(s)
            elif s == ')':
                if (i < len(units) - 1 and not units[i + 1].isdigit()) or i == len(units) - 1:
                    index = len(stack) - 1
                    while index >= 0 and stack[index] != '(':
                        index -= 1
                    stack.pop(index)
                else:
                    stack.append(s)
            elif s.isdigit():
                num = int(s)
                if stack[-1] == ')':
                    index = len(stack) - 2
                    while index >= 0 and stack[index] != '(':
                        stack[index][1] *= num
                        index -= 1
                    stack.pop(index)
                    stack.pop(-1)
                else:
                    stack[-1][1] = num
            else:
                stack.append([s, 1])
        m = {}

        print stack
        for (atom, number) in stack:
            m[atom] = m.setdefault(atom, 0) + number
        result = ''
        keys = m.keys()
        keys.sort()
        for k in keys:
            result += k + (str(m[k]) if m[k] > 1 else '')

        print result
        return result

    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """

        return self.sol2(formula)


s = Solution()
s.sol2("K4(ON(SO3)2)2")
s.countOfAtoms("(ON(SO3)2)2")
s.countOfAtoms("((O(O(O3)2)2))")
s.sol2('O(O(O3)2)2')
s.sol2('H2O')
s.countOfAtoms("Mg(OH)20")
