class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for s in strs:
            for idx, ss in enumerate(s):
                if len(prefix) > idx:
                    if prefix[idx] != ss:
                        prefix = prefix[0:idx]
            prefix = prefix[0:len(s)]
        return prefix