#!/usr/bin/python
# -*- coding: utf-8 -*-
# LastName:Raesly
# FirstName:John
# Email:john.raesly@colorado.edu
# Comments: Collaborators: Pat Andresen, Connor Mcguinness 

from __future__ import print_function
import sys


# We will use a class called my trie node

class MyTrieNode:

    # Initialize some fields
    def __init__(self, isRootNode):

        # The initialization below is just a suggestion.
        # Change it as you will.
        # But do not change the signature of the constructor.

        self.isRoot = isRootNode
        self.isWordEnd = False  # is this node a word ending node
        self.isRoot = False  # is this a root node
        self.count = 0  # frequency count
        self.next = {}  # Dictionary mappng each character from a-z to the child node
        
    def addWord(self, w):
        word = w
        for letter in word:
            if letter not in self.next:
                self.next[letter] = MyTrieNode(False)
            self = self.next[letter]
        self.isWordEnd = True
        self.count += 1

    def lookupWord(self, w):

        # Return frequency of occurrence of the word w in the trie
        # returns a number for the frequency and 0 if the word w does not occur.
        # YOUR CODE HERE

        word = w
        for letter in word:
            if letter not in self.next:
                return False
            else:
                self = self.next[letter]

        return self.count

    def autoHelper(self, w, lst = []): 
		word = w
		for key,val in self.next.items():
			wk = word + key
			if self.next[key].isWordEnd == True:
				lst.append((wk, self.next[key].count))
			self.next[key].autoHelper(wk, lst)
		return lst

    def autoComplete(self, w):

        # Returns possible list of autocompletions of the word w
        # Returns a list of pairs (s,j) denoting that
        #         word s occurs with frequency j

        word = w
        lst = []
        for letter in word:
            if letter not in self.next:
				#base case
                return []
            self = self.next[letter]
        if self.isWordEnd:
			#create tuple
            lst.append((word, self.count))
        return list(self.autoHelper(word, lst))


if __name__ == '__main__':
    t = MyTrieNode(True)
    lst1 = [
        'test',
        'testament',
        'testing',
        'ping',
        'pin',
        'pink',
        'pine',
        'pint',
        'testing',
        'pinetree',
        ]

    for w in lst1:
        t.addWord(w)

    j = t.lookupWord('testy')  # should return 0
    j2 = t.lookupWord('telltale')  # should return 0
    j3 = t.lookupWord('testing')  # should return 2
    lst3 = t.autoComplete('pi')
    print('Completions for "pi" are : ')
    print(lst3)

    lst4 = t.autoComplete('tes')
    print('Completions for "tes" are : ')
    print(lst4)


			

			
