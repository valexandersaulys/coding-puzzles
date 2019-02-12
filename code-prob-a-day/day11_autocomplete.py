#! usr/bin/python4
"""
Good morning! Here's your coding interview problem for today. 

This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and
a set of all possible query strings, return all strings in the set
that have s as a prefix. 

For example, given the query string de and the set of strings [dog,
deer, deal], return [deer, deal]. 

Hint: Try preprocessing the dictionary into a more efficient data
structure to speed up queries. 
"""
class TrieNode(object):

    def __init__(self,char):
        self.char = char
        self.children = []
        self.word_finished = False  # if this is the end of a word or not
        self.counter = 1

    def __str__(self):
        return "%s" % self.char


def add(root, word: str):
    node = root
    for char in word:
        found_in_child = False
        for child in node.children:
            if child.char == char:
                node = child
                found_in_child = True
                break
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            node = new_node
            print(node.children)
    node.word_finished = True

def find_prefix(root, prefix: str):
    node = root
    if not root.children:  # if we have no children, return False
        return False
    for char in prefix: 
        char_not_found = True
        for child in node.children:
            if child.char == char:
                char_not_found = False
                node = child
                break
        if char_not_found:
            return False
    return True;
    

def autocomplete(s):
    """
    I tried a trie but it didn't fucking work becuase shit is so gay
    """
    
    pass


if __name__ == "__main__":

    root = TrieNode('*')
    add(root, "hackathon")
    add(root, 'hack')

    print([str(x) for x in root.children])

    print(find_prefix(root, 'hac'))
    print(find_prefix(root, 'hack'))
    print(find_prefix(root, 'hackathon'))
    print(find_prefix(root, 'ha'))
    print(find_prefix(root, 'hammer'))
    
    #print(autocomplete(s="",prefixes=[]))
