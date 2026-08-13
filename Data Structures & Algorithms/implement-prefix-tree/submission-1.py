class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            # not in hashmap yet
            if c not in cur.children:
                # this is how we insert characters
                cur.children[c] = TrieNode()
            # if not, move to that character
            cur = cur.children[c]
        # cur is now set to last character
        cur.endOfWord = True


    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        
        if cur.endOfWord:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        
        return True