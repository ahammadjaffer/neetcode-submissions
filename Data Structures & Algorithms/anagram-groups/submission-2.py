class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        seen = []
        process = lambda x: ''.join(sorted(list(x)))
        for i in range(len(strs)):
            if strs[i] not in seen:
                temp = [strs[i]]
                if i+1 < len(strs):
                    for j in range(i+1, len(strs)):
                        if process(strs[i]) == process(strs[j]):
                            temp.append(strs[j])
                seen.extend(temp)
                result.append(temp)
        return result
            