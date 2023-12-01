# your code goes here!
import ipdb

class Anagram:
    def __init__(self, word="someword"):
        self.word = word
    
    def match(self, word_list):
        split_provided_word = [letter for letter in self.word]
        matched_word = []
        for word in word_list:
            split_word = [letter for letter in word]
            if sorted(split_provided_word) == sorted(split_word):
                matched_word.append(word)
        return matched_word
            
        


listen = Anagram("listen")
listen.match(['enlists', 'google', 'inlets', 'banana'])

