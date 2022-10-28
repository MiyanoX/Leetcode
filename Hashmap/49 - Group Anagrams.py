class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}                                      # build empty hash map
        for str in strs:
            sort_str = "".join(sorted(list(str)))   # transform string to sorted one
            if sort_str in d:                       # add string to hashmap
                d[sort_str].append(str)
            else:
                d[sort_str] = [str]
        return d.values()                           # return values list of hashmap