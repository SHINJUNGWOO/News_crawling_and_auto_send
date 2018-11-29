from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

# JTBC Parser
#http://fs.jtbc.joins.com//RSS/morningand.xml

class news_crawler:
    def __init__(self):
        self.url="http://fs.jtbc.joins.com//RSS/morningand.xml"
        self.full_string = ""

        self.process()

    def process(self):
        self.response=urllib.request.urlopen(self.url)
        self.soup=BeautifulSoup(self.response,'html.parser')
        self.result=self.soup.select("title")

        for result in self.result:
            self.full_string+=(result.string+"\n")

        print(self.full_string)


a=news_crawler()