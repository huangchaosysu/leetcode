class Solution:
    # a + 1 / b 必定是最简分数，所以不用求GCD了。 （前提：a是整数，b是一个最简分数） 因为b是最简分数，所以 1 / b肯定也是一个最简分数，加上一个整数仍然是最简分数：（ab + 1）/ b = a …… 1
    def fraction(self, cont):  # cont list[int]
        if len(cont) == 1:
            return [cont[0], 1]

        rt = [cont[-1], 1]
        i = len(cont) - 2
        while i >= 0:
            rt[0], rt[1] = rt[1], rt[0]
            rt = [cont[i] * rt[1] + rt[0], rt[1]]
            i -= 1

        return rt


if __name__ == "__main__":
    # cont = [3, 2, 0, 2]
    s = Solution()
    # print(s.fraction(cont))
    # #
    # cont = [0, 0, 3]
    # print(s.fraction(cont))

    cont = [0, 2147483647]
    print(s.fraction(cont))
