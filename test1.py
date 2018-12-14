from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import re

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
        self.result=self.soup.select("item")

        self.data = {}
        # for result in self.result:
        #     self.full_string+=(result.string+"\n\n")

        #print(self.result)
        p=re.compile("<link/>.*<description>")
        for line in self.result:
            title=str(line.find_all("title"))
            link=p.findall(str(line))
            title=title[8:-9]
            link=link[0][7:-13]
            self.data[str(title)]=link

        #print(self.data)

a=news_crawler()
