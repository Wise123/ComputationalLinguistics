from urllib2 import urlopen
from bs4 import BeautifulSoup
import re
html_doc = urlopen('http://www.dns-shop.ru/catalog/17a892f816404e77/noutbuki/').read()
soup = BeautifulSoup(html_doc)
collect = soup.find('div', 'catalog-category')
opisanie = collect.findAll('div','price_g')
opisanie1 = collect.findAll('div','item-name')
opisanie2 = collect.findAll('div','item-desc')
i=0
k=0
j=0
while i<len(opisanie):
    print opisanie[i].get_text()
    i=i+1
while j<len(opisanie1):
    print opisanie1[j].get_text()
    j=j+1
while k<len(opisanie2):
    print opisanie2[k].get_text()
    k=k+1