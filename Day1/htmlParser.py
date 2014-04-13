#Opens a local HTML document and prints out tags+data
#Libs Needed - HTMLParser & urllib


import urllib
feed=urllib.urlopen('file:///E:/Mtech%20Python%20Sessions/test.html')
a=feed.read()

from HTMLParser import HTMLParser

class myParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print tag
    def handle_endtag(self, tag):
        print tag
    def handle_data(self, data):
        print data
