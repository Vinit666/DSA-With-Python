class Solution:

    def build_1(self, target, n):
        result = []
        ml = [i for i in range(1, n + 1)]

        i = 0
        for j in range(target[-1]):
            if ml[j] == target[i]:
                result.append("Push")
                if i < len(target) - 1:
                    i += 1
            else:
                result.append("Push")
                result.append("Pop")

        return result

    def buildArray(self, target, n):
        result = []

        i = 0
        for j in range(target[-1]):
            if j + 1 == target[i]:
                result.append("Push")
                if i < len(target):
                    i += 1
            else:
                result.append("Push")
                result.append("Pop")

        return result


s1 = Solution()
print(s1.build_1(target=[1, 3], n=4))
print(s1.buildArray(target=[1, 3], n=4))
