# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import html2text
import urllib2
from bs4 import BeautifulSoup

def getPage(url):
    res = urllib2.urlopen(url)
    html = res.read()
    soup = BeautifulSoup(html)
    tt = soup.find('table')
    content = tt.find('td', {"valign" : "top", "width" : "600"})
    return html2text.html2text(content.decode_contents())

# <codecell>

index = getPage('http://www.greenteapress.com/thinkstats/html/index.html')

# <codecell>

pages = 'http://www.greenteapress.com/thinkstats/html/thinkstats%s.html'

# <codecell>

chpts = ['%03d' % (x+1) for x in range(11)]
#allchpts = [getPage(pages % x) for x in chpts]

# <codecell>

allchpts = []
for x in chpts:
    print pages % x
    allchpts.append(getPage(pages % x))

# <codecell>

#write files...
def writeFile(item, name):
    fwrite = open("scratch/"+name, 'w')
    fwrite.write(item.encode('utf-8'))
    fwrite.close()
    return None

writeFile(index, 'index.md')
for i,x in enumerate(allchpts):
    writeFile(x, "%03d.md" % (i+1))

