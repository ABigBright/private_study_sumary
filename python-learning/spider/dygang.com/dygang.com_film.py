import requests
import lxml.etree as etree

link = 'http://www.dygang.com'
me = 'GET'
enc = 'gbk'

g_film_info = {
    id: 0,
    'name': '',
    'dl_link': []
}

g_film_info_list = []

def get_response(me=None, lnk=None, enc=None):
    response = requests.request(me, lnk)
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

def parse_film_accesslink():
    film_class = parse_film_class()
    select_class = input('选择电影类别：')
    select_film_page = input('指定电影页数：')
    response = get_response(me, film_class[int(select_class)][1] + 'index_2.htm', enc)
    xpath_result = parse_html_from_xpath(response, '//a[@class="classlinkclass"]')
    film_accesslink = []
    for i, j in enumerate(xpath_result):
        film_accesslink.append([j.text, j.get('href')])
    return film_accesslink

def main():
    pass

if __name__ == '__main__':
    main()
