from Parse import *
from Process import *
from operator import itemgetter
import sys
import pydoc 

class Main:

    def urlfetch(self):
        # check if the URL has been passed
        if(len(sys.argv) == 1 ): 
            print 'Usage : python main.py [url]'
            sys.exit()

        # fetching from the URL
        try:
            h = Parse(sys.argv[1])
            self.parsing(h)
        except ValueError as e :
            print e
            sys.exit()
            
    def parsing(self,h):
        
        
        # bag of word of content
        content = h.getContent()
        t=Text()
        content=t.preprocess(content)
        content = t.sortBag(content)
        content=content[:20]
        
           
        # bag of word on title, meta-keywords, heading
        #header=title+ " "+keyword
        #for h in hx: header+=" "+h
        header = h.getHeaders()
        header = t.preprocess(header)
        header=t.sortBag(header)
        header=header[:10]
        
        #merging the two bags for final result
        self.merge(header,content)
        

        # merging the content and the header into one list giving the heading, metatag and title more weights
    def merge(self,header,content):
        d=Text()
        finalres = d.mergeList(header,content,3)
        x=sorted(finalres,key=itemgetter(1),reverse=True)
        x=x[:7]
        print "URL : "+sys.argv[1]
        print 'Topics :',

        for w in x:
            print w[0]+",",
            print ''

if __name__ == "__main__":
    m=Main()
    m.urlfetch()
