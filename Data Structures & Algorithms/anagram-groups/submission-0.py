class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            sortedWord = ''.join(sorted(s)) # sorts the word into a list of each character and combines them back together
            hashmap[sortedWord].append(s) # a hash map where the key is the sorted word. the value is a list of the words that are anagrams to that sorted word
        return list(hashmap.values()) # returns the hash map values as a list