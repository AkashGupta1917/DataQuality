# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 17:38:06 2023

@author: Divya.Saraswat and Akash Gupta
"""


from textblob import TextBlob

class IncorrectData():
    
    def correct_sentence_spelling(sentence):
        
        print('original', sentence)
        sentence = TextBlob(sentence)
    
        result = sentence.correct()
    
        print('correction',result)
