class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        We want to make a hashmap where the key value pair is
        key: sorted char
        value: original word

        then we need to return all the vals as a list
        """
        hashmap = {}
        for word in strs:
            sorted_word = sorted(word)
            sorted_word = ''.join(sorted_word)
            if sorted_word in hashmap:
                hashmap[sorted_word].append(word)
            else:
                hashmap[sorted_word] = [word]
        return list(hashmap.values())