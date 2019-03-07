#! usr/bin/env python3
import pprint

pp = pprint.PrettyPrinter(indent=2)

class SuffixTrie:

    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        i = len(string)-1
        
        while i >= 0:
            c = string[i]
            if i == len(string)-1:
                self.root[c] = {'*':True}
                i -= 1
                continue
			
	    # create an entry if we're not in yet
            if c not in self.root:
                self.root[c] = {}

            self.root[c].update({string[i+1]: dict(self.root[string[i+1]])})

            i -= 1
                

    def contains(self, string):
        i = 0
        d = self.root
        
        while i < len(string):
            c = string[i]
            d = d.get(c,0)
            
            if d == 0:
                return False # not found
            
            i += 1
        return True


if __name__ == "__main__":
    sf = SuffixTrie('babc')
    pp.pprint(sf.root)
    print(sf.contains('abc'))
