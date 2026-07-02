class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_hash = {}

        for i in strs:
            if str(sorted(i)) not in anagram_hash :
                anagram_hash[str(sorted(i))] = [i]
            else:
                anagram_hash[str(sorted(i))].append(i)
    
        print(anagram_hash)
        return list(anagram_hash.values())
        