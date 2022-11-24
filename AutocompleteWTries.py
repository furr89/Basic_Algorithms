# Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

    # Add a child node in this Trie
    def insert(self, char):

        # Adds the character in the dictionary and gives it a TrieNode value 
        if char not in self.children:
            self.children[char] = TrieNode()

    # Helper for suffixes()
    def search_suffixes(self, trie_node, suffix, suff_list):

        # If at the current node, there is a complete word, append it to the list
        if trie_node.is_word:
            suff_list.append(suffix)

        # Otherwise, keep searching down the trie
        for char, node in trie_node.children.items():
            self.search_suffixes(node, suffix + char, suff_list)

        return suff_list

    # Runs a recursive function that collects the suffix for complete words
    def suffixes(self, suffix = ''):

        suff_list = []
        current_node = self

        if not current_node:
            return None
        
        suff_list = current_node.search_suffixes(current_node, suffix, suff_list)       

        print(suff_list)
        return suff_list


# The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Add a word to the Trie
    def insert(self, word):
        
        current_node = self.root

        # Inserts each character of the word
        for char in word:
            current_node.insert(char)

            current_node = current_node.children[char]

        current_node.is_word = True

    # Find the Trie node that represents this prefix
    def find(self, prefix):

        # Turn input to string if not already
        if type(prefix) != str:
            print("Null")
            return None
        
        current_node = self.root

        # Navigate through Trie and stop at the end of prefix
        for char in prefix:

            # Checks for chars not present
            if char not in current_node.children.keys():
                print("Not Found")
                return None

            current_node = current_node.children[char]

        #print(current_node.children.keys())
        return current_node


MyTrie = Trie()

wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]

# Insertions tests
for word in wordList:
    MyTrie.insert(word)


# Test cases for finding when input is as expected
MyTrie.find('tri') # Should return following letters
MyTrie.find('trigger') # No following letters come after
MyTrie.find('') # Should return all first letters in the trie

# Cases when the input is not found; when a letter has been added but not found after a valid search
# For example: 'ant' is a word in the trie but not 'ants'
MyTrie.find('x')
MyTrie.find('fr')
MyTrie.find('ants')

MyTrie.find(' ') # Should return not found

# Edge cases. Should return None
MyTrie.find(35) 
MyTrie.find(None)

# Suffixes tests
MyTrie.find('fu').suffixes()
MyTrie.find('tr').suffixes()
MyTrie.find('tri').suffixes()
MyTrie.find('trigger').suffixes()

