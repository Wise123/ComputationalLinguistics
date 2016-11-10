html_doc = urllib.request.urlopen(dnsHomeUrl + laptopsAndTablets['href'] + '?p=' + pagesNumber).read()
soup = BeautifulSoup(html_doc)
opisanie = soup.find_all('div',class_="price_g")
opisanie1 = soup.find_all('div',class_="item-name")
opisanie2 = soup.find_all('div',class_="item-desc")
i=0
k=0
j=0
while i<len(opisanie):
    print (opisanie[i].get_text())
    i=i+1
while j<len(opisanie1):
    print (opisanie1[j].get_text())
    j=j+1
while k<len(opisanie2):
    print (opisanie2[k].get_text())
    k=k+1