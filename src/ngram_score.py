'''
Allows scoring of text using n-gram probabilities
17/07/12
'''
from math import log10

class ngram_score(object):
    def __init__(self,ngramfile,sep=' '):
        ''' load a file containing ngrams and counts, calculate log probabilities 
            'AAAA' -> log(num_from_file / sum (all numbers_from_file)) '''

        self.ngrams = {}
        for line in file(ngramfile):
            key,count = line.split(sep) 
            self.ngrams[key] = int(count)
        self.L = len(key)
        self.N = sum(self.ngrams.itervalues())
        #calculate log probabilities
        for key in self.ngrams.keys():
            self.ngrams[key] = log10(float(self.ngrams[key])/self.N)
        self.floor = log10(0.01/self.N)

    def score(self,text):
        ''' compute the score of text 
            split text to quadgrams, and sum scores for each quadgram'''
        score = 0
        ngrams = self.ngrams.__getitem__
        for i in xrange(len(text)-self.L+1):
            if text[i:i+self.L] in self.ngrams: score += ngrams(text[i:i+self.L])
            else: score += self.floor          
        return score

# usage example
#
# import ngram_score as ns
# fitness = ns.ngram_score('quadgrams.txt')
# print fitness.score('HELLOWORLD')
