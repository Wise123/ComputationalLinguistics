from bs4 import BeautifulSoup
import urllib
import urllib.request

#функция для получения супа страницы по url
def getSoupByUrl(url):
    request = urllib.request.Request(dnsHomeUrl)
    opener = urllib.request.build_opener()
    response = opener.open(request)
    html_doc = urllib.request.urlopen(dnsHomeUrl).read()
    return BeautifulSoup(response.read())


dnsHomeUrl = 'http://www.dns-shop.ru' #начинаем с домашней страницы потому что при переходе к ноутбукам сайт даёт нам айдишник

mainPage = getSoupByUrl(dnsHomeUrl)#получаем суп главной страницы
menuCatalog = mainPage.find_all(id="menu-catalog")[0]# получаем меню-каталог
laptopsAndTablets = menuCatalog.find_all('div', class_="sub-wrap")[0].findAll('a')[0]#получаем элемент-ссылку на страницу с ноутбуками

# я не знаю как выяснить общее количество страниц, пока оставим это пользователю
pagesNumber = input('сколько страниц вы хотите загрузить?')
print(dnsHomeUrl + laptopsAndTablets['href'] + '?p=' + pagesNumber)
# получаем суп страницы с ноутбуками
laptopsPage = getSoupByUrl(dnsHomeUrl + laptopsAndTablets['href'] + '?p=' + pagesNumber)

#print(laptopsPage.prettify())1

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