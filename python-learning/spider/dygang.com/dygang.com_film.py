import time
import sys
import os
import requests
import lxml.etree as etree
from prettytable import PrettyTable

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

def get_response(me=None, lnk=None, enc=None):
    response = requests.request(me, lnk, headers=headers)
    response.encoding = enc
    return response

def parse_html_from_xpath(response: object = None, xpath: object = None) -> object:
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

def get_film_class_select(film_class):
    select = int(input('Please input the film class ID: '))
    return 0 if select >= len(film_class) else select

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

def parse_all_film_access_link():
    film_class = parse_film_class()
    film_class_print(film_class)
    select = get_film_class_select(film_class)
    pages = parse_film_pages(film_class, select)
    film_access_link = []
    for page in range(1, pages):
        film_access_link = parse_film_access_link(film_class, select, str(page))
        parse_film_download_link(film_access_link)
    return film_access_link

def parse_film_download_link(film_access_link):
    all_film_download_link = []
    for i, j in film_access_link:
        xpath_result = parse_html_from_xpath(get_response(me, j, enc), '//td[@style="word-break: break-all; line-height: 18px"]/a')
        one_film_download_link = []
        one_film_download_link.append(i)
        for k in xpath_result:
            one_film_download_link.append(k.get('href'))
        all_film_download_link.append(one_film_download_link.copy())
    for name, *links in all_film_download_link:
        print(name + ":")
        for link in links:
            print(">> " + link)
        print("\r\n")

def main():
    parse_all_film_access_link()

if __name__ == '__main__':
    main()
