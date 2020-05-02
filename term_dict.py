import re

class TermDict:

    def __init__(self):
        self.term_dict = {}
        self.ranking = {'title': 50, 'h1': 40, 'h2': 30, 'h3': 20, 'b': 10, 'strong': 10, 'i': 5, 'em': 5}


    def update(self, soup):
        for item in soup.recursiveChildGenerator():
            if item.string and item.name:
                words = self.processText(item.string)
                self.updateTermDict(words, self.ranking[item.name] if item.name in self.ranking else 1)
            elif item.string:
                words = self.processText(item.string)
                self.updateTermDict(words)


    def processText(self, text):
        words = []
        for word in text.strip().split():
            word = word.lower()
            # DO TOKENIZING / STOP WORDS / STEMMING HERE

            if not re.match("^(?:\w|\d)+$", word):
                continue

            words.append(word)
        return words


    def updateTermDict(self, words: [str], amt = 1):
        for word in words:
            if word not in self.term_dict:
                self.term_dict[word] = amt
            else:
                self.term_dict[word] += amt

    
    def getTermDict(self):
        return self.term_dict