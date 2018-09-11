import requests
import time
import lxml.etree as etree

link = 'http://www.dygang.com'
me = 'GET'
enc = 'gbk'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-GB,en;q=0.5',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'
}

g_film_class = []
g_film_access_link = []

def get_response(me=None, lnk=None, enc=None):
    response = requests.request(me, lnk, headers=headers)
    response.encoding = enc
    return response

def parse_html_from_xpath(response=None, xpath=None):
    html = etree.HTML(response.text, etree.HTMLParser())
    xpath_result = html.xpath(xpath)
    return xpath_result

def parse_film_class():
    response = get_response(me, link, enc)
    xpath_result = parse_html_from_xpath(response, '/html/body/table[3]/tbody/tr/td/a')
    film_class = []
    for i, j in enumerate(xpath_result):
        if 0 == i or len(xpath_result) - 1 == i:
            continue
        film_class.append([j.text, j.get('href')])
    return film_class

def film_class_print(film_class):
    for i, j in enumerate(film_class):
        print(i, ' - ', j[0])

def get_film_class_select():
    select = int(input('Please input the film class ID: '))
    print(g_film_class)
    return 0 if select >= len(g_film_class) else select

def parse_film_access_link(film_class, select, page=2):
    print('Start parse the %s page of %s' %(page, film_class[select][0]))
    if 1 == page:
        response = get_response(me, film_class[select][1] + 'index.htm', enc)
    else:
        response = get_response(me, film_class[select][1] + 'index_' + page + '.htm', enc)
    xpath_result = parse_html_from_xpath(response, '//a[@class="classlinkclass"]')
    film_access_link = []
    for i, j in enumerate(xpath_result):
        film_access_link.append([j.text, j.get('href')])
    return film_access_link

def parse_film_pages(film_class, select):
    response = get_response(me, film_class[select][1], enc)
    element = parse_html_from_xpath(response, '//a[@title="Total record"]/b')
    return int(element[0].text[:-1]) + 1

def parse_all_film_access_link(film_class):
    pass

def main():
    g_film_class = parse_film_class()
    film_class_print(g_film_class)
    select = get_film_class_select()
    select = 13
    pages = parse_film_pages(g_film_class, select)
    for page in range(1, pages):
        film_access_link = parse_film_access_link(g_film_class, select, str(page))
        g_film_access_link.extend(film_access_link)
        time.sleep(1)
    for i in g_film_access_link:
        print(i)


if __name__ == '__main__':
    main()
