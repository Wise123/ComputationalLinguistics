from bs4 import BeautifulSoup
import urllib
import urllib.request
import json


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

fullDescription = []

#print(len(prices))

for i in range(len(prices)):
    outputData.append({
        'price': prices[i].get_text(),
        'name': names[i].get_text(),
        'shortDescription': shortDescriptions[i].get_text(),
        'link': links[i]['href']
    })


'''
for i in outputData:
    print(i['price'])
    print(i['name'])
    print(i['shortDescription'])
    print(i['link'])
    print('')

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


print(len(outputData))

for i in range(len(outputData)):
    charLink = dnsHomeUrl + outputData[i]['link'] + "characteristics/"
    print(charLink)
    childPage = getSoupByUrl(charLink)
    charTableElem = childPage.find_all('table', class_="table-params table-no-bordered")[0]  # получение таблицы с характеристиками
    specif = childPage.find_all('div', class_="price_item_description")
    for x in charTableElem.find_all('tr'):  # идем по строкам
        if (len(x.find_all('td')) == 1):  # если в строке только 1 td
            ex = x.find_all('td')[0].text
            ex2 = ""
        else:
            ex = x.find_all('td')[0].find_all('a')[0].text
            ex2 = x.find_all('td')[1].text

        strForJson = "\"" + ex + "\":\"" + ex2 + "\""
        fullDescription.append(strForJson)

    print(fullDescription)
    # outputData.append({'fullDescription': fullDescription[i]})

with open('dataJson.txt', 'w', encoding='utf-8') as f:
  f.write(json.dumps(outputData, indent=4, ensure_ascii=False))