from bs4 import BeautifulSoup
import urllib
import urllib.request


# функция для получения супа страницы по url
def getSoupByUrl(url):
    html_doc = urllib.request.urlopen(url).read()
    return BeautifulSoup(html_doc, "html.parser")

dnsHomeUrl = 'http://www.dns-shop.ru'  # начинаем с домашней страницы потому что при переходе к ноутбукам сайт даёт нам айдишник

mainPage = getSoupByUrl(dnsHomeUrl)  # получаем суп главной страницы
menuCatalog = mainPage.find_all(id="menu-catalog")[0]  # получаем меню-каталог
laptopsAndTablets = menuCatalog.find_all('div', class_="sub-wrap")[0].findAll('a')[0]  # получаем элемент-ссылку на страницу с ноутбуками

laptopsPage = getSoupByUrl(dnsHomeUrl + laptopsAndTablets['href'])
# print(laptopsPage.prettify())
prices = laptopsPage.find_all('div',class_="price_g")
names = laptopsPage.find_all('div',class_="item-name")
shortDescriptions = laptopsPage.find_all('div',class_="item-desc")
links = laptopsPage.find_all('a',class_="ec-price-item-link")
i = 0

outputData = []

for i in range(len(prices)):
    outputData.append({
                            'price': prices[i].get_text(),
                            'name': names[i].get_text(),
                            'shortDescription': shortDescriptions[i].get_text(),
                            'link': links[i]['href']
                       })

for i in outputData:
    print(i['price'])
    print(i['name'])
    print(i['shortDescription'])
    print(i['link'])
    print('')
'''
структура данных:
[
    {
        'price':'12 990 p',
        'name':'11.6" Ноутбук Prestigio Smartbook 116A черный',
        'shortDescription':'[HD, 1366x768, TN+film, Intel Atom Z3735F, 4x1.333 ГГц, RAM 2 Гб, SSD 32 Гб, Intel HD, Wi-Fi, BT, Win 10]',
        'link':'/product/e27e187d4cab3330/116-noutbuk-prestigio-smartbook-116a-cernyj/'
    }
]
'''
