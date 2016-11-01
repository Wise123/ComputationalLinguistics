from bs4 import BeautifulSoup
import urllib
import urllib.request

#функция для получения супа страницы по url
def getSoupByUrl(url):
    request = urllib.request.Request(dnsHomeUrl)
    opener = urllib.request.build_opener()
    response = opener.open(request)
    return BeautifulSoup(response.read())


dnsHomeUrl = 'http://www.dns-shop.ru' #начинаем с домашней страницы потому что при переходе к ноутбукам сайт даёт нам айдишник

mainPage = getSoupByUrl(dnsHomeUrl)#получаем суп главной страницы
menuCatalog = mainPage.find_all(id="menu-catalog")[0]# получаем меню-каталог
laptopsAndTablets = menuCatalog.find_all('div', class_="sub-wrap")[0].findAll('a')[0]#получаем элемент-ссылку на страницу с ноутбуками

# я не знаю как выяснить общее количество страниц, пока оставим это пользователю
pagesNumber = input('сколько страниц вы хотите загрузить?')
# print(dnsHomeUrl + laptopsAndTablets['href'] + '?p=' + pagesNumber)
# получаем суп страницы с ноутбуками
laptopsPage = getSoupByUrl(dnsHomeUrl + laptopsAndTablets['href'] + '?p=' + pagesNumber)

print(laptopsPage.prettify())