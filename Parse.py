import urllib2
import re
from bs4 import BeautifulSoup
from Process import *
import bs4


eratio = 0.75

class Parse:
	
    def __init__(self,url):
        try:
            opener = urllib2.build_opener()
            opener.addheaders = [('Accept-Charset', 'utf-8')]
            content = opener.open(url, timeout=5).read()
        except:
            raise ValueError('Unable to get content from '+url)
		
        try:
            soup = BeautifulSoup(content)
            soup.encode('utf-8')
            [s.replaceWith(" ") for s in soup('script')]
        except:
            raise ValueError('Unable to parse the content')
        [s.replaceWith(" ") for s in soup('link')]
        [s.replaceWith(" ") for s in soup('style')]

        invalid_tags = ['b', 'i', 'u', 'strong', 'a']
        for tag in invalid_tags: 
            for match in soup.findAll(tag):
                match.replaceWithChildren()

        self.soup = soup;
        pass;
    #text preprocessing
    def parseText(self,text):
        text = text.encode('utf-8','ignore')
        text = text.lower()
        text = re.sub(r'([^\s\w]|_|\n|\t|\r)+', ' ', text)
        text = re.sub(' +',' ',text)
        return text
    def getHeaders(self):
        title=self.getTitle()
        keyword=self.getKeyword()
        hx=self.getHeading()
        header=title+ " "+keyword
        for h in hx: header+=" "+h
        return header
        
    def getTitle(self):
        if(self.soup.title == None):
            return "";
        else:
            txt = self.parseText(self.soup.find('title').get_text())
            return re.sub(r'\W+', ' ', txt)

    def getKeyword(self):
        tag = self.soup.find("meta", {"name":"keywords"})
        if(tag== None):
            return "";
        else:
            return self.parseText(tag['content']);

	#get headings 
    def getHeading(self):
        ans = []
        tag = self.soup.find(['h1','h2','h3','h4'])
        if(tag != None):
            ans.append(self.parseText(tag.get_text()))
        return ans;
    
    #get content
    def getContent(self):
        res=[]
        str = ""
        self.getRecurContent(None,res)
        for txt in res: 
            str+= txt+" "
        return self.parseText(str)

	# Recursively parse the HTML tree until density between tag and text is equal
    def getRecurContent(self,current,res):
        if(current == None):
            current = self.soup
		
        if(len(str(current)) == 0):
            return
        ratio = len(current.get_text())/float(len(str(current)))
        if(ratio > eratio):
            res.append(self.parseText(current.get_text())+" ")
        else:
            for i in range(len(current.findChildren(recursive = False))):
                self.getRecurContent(current.findChildren(recursive = False)[i],res)
	

