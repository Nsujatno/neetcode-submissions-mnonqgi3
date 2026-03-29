class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        First create an array of the characters in the string
        then sort the array
        and check if both arrays are equal
        if they are equal, return true else return false
        """
        # arrays
        first_word = []
        second_word = []
        
        for char in s:
            first_word.append(char)
        for char in t:
            second_word.append(char)

        # sort arrays
        first_word.sort()
        second_word.sort()

        # check if the two arrays are equal
        if first_word == second_word:
            return True
        else:
            return False