from Parse import *
import nltk
from collections import defaultdict
import re
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
stemmer = SnowballStemmer('english')

stop = set(stopwords.words('english'))
punctuations = ['!', '"', '#', '$', '%', '&', '\'', ',', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=',
                '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~','a','e','i','o','u']


# output dictionary of words along with their frequency count after removing the stop words and punctuations
#output= {'words1':1,'words2':2,'words3':3}
class Text:
    #tokenise the words,remove the stopwords and punctuation,part of speech tagging and return a list of important words containing nouns and adjectives
    def preprocess(self,txt):
        tempwordlist=[]
        finalWords= []
        txts = nltk.word_tokenize(txt)
        for d in txts:
            stemmer.stem(d)
            if d not in stop and punctuations:
                tempwordlist.append(d)
        posTags = nltk.pos_tag(tempwordlist)
        #print posTags
        for i in posTags:
            if i[1] in ['NN','JJ']:
                finalWords.append(i[0])
        ve=self.getdict(finalWords)
        return ve
    
    #function returns  a dictionary of important words along with their frequencies {'word1':2,'word2':1,'word3':4}      
    def getdict(self,finalWords):
        counts = defaultdict(int)
        for j in finalWords:
            counts[j]+=1
        return counts
    
    #returns a list of tuple of word and their frequencies sorted based on their frequencies [('words3',3),('words2',2),('word1',1)]
    def sortBag(self,bag):
        res=[]
        for w in sorted(bag, key=bag.get, reverse=True):
            res.append((w, bag[w]))
        return res

# merge the 2 lists
    def mergeList(self,list1,list2,weight=1):
        counts = {}
        for b in list1: 
            counts[b[0]] = b[1]*weight
        for b in list2: 
            if(b[0] in counts): 
                counts[b[0]]+=b[1]
            else:
                counts[b[0]]=b[1]
	# print counts
        ans = []
        for k in counts:
            ans.append((k,counts[k]))
        return ans

