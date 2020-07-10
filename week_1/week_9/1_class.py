from sys import stdin
import copy


class Matrix:
    def __init__(self, m_list):
        self.val = copy.deepcopy(m_list)

    def __str__(self):
        res = ""
        j = 0
        for i in self.val:
            res += '\t'.join(map(str, i))
            j += 1
            if j < len(self.val):
                res += '\n'
        return res

    def size(self):
        return len(self.val), len(self.val[0])


#
# a = list([[1, 2], [3, 4], [5, 6]])
# # print(*a)
# m = Matrix(a)
# print(m.size())
exec(stdin.read())
