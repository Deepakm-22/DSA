
class Solution:
    def longestCommonPrefix(self, strs):
        prefix = strs[0]

        for w in strs[1:]:
            while not w.startswith(prefix):
                prefix = prefix[:-1]

                if prefix == "":
                    return ""

        return prefix