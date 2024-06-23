class TreeNode:
    def __init__(self):
        self.children = {} # {char : TreeNode()}
        self.end_of_word = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()


    def insert(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TreeNode()
            curr = curr.children[char]
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root

        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True
        
        
