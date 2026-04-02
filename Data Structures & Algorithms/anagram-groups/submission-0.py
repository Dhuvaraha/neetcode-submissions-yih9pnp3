class Solution:
    def groupAnagrams(self, strs):
        from collections import defaultdict
        
        groups = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))  # sort and make string
            groups[key].append(word)

        return list(groups.values())