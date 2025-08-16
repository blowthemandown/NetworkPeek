class TextParser(object):
    def __init__(self, raw):
        self.rawtext = raw
        self.paragraph = raw.splitlines()#that SHOULD give a list of strings, each a line from the output
        

    def __Str__(self):
        print(self.rawtext)#not this?

    def lineIterator(self, search):#make private with _?
        for x in self.paragraph:
            if x.startswith(search): return x
        return ""#maybe return something else if it can't be found
    
    def printMacAdd(self):#                                                             maybe time to start with my graphs!
        line = self.lineIterator("")

    def printIPAdd(self):
        line = self.lineIterator("IPv4")#might need to begin that with an indentation

    
 



