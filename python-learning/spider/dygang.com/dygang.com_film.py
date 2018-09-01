import sys
import requests
import re
import time
import bs4
from bs4 import BeautifulSoup
import prettytable
from prettytable import PrettyTable

link = 'http://www.dygang.com'
me = 'GET'
enc = 'gbk'

def get_rsps(me=None, lnk=None, enc=None):
    rsps = requests.request(me, lnk)
    rsps.encoding = enc
    return rsps

def parse_html_element(rsps=None, elemt=None, attrs=[]):
    bs = BeautifulSoup(rsps.text, "html.parser")
    tmp_slct = bs.select('td[%s] > a' %(attrs[0]))
    return tmp_slct

def parse_dygang_film_type(elemt_content=None):
    elemt_content.pop(0)
    elemt_content.pop(-1)
    tmp_lst = []
    tmp_dic = {'id':'', 'name':'', 'link':''}
    for i,j in enumerate(elemt_content):
        t1 = re.findall('<a href="(.*)">(.*)</a>.*', str(j))[0]
        tmp_dic['id'] = i
        tmp_dic['name'] = t1[1]
        tmp_dic['link'] = t1[0]
        tmp_lst.append(tmp_dic.copy())
    return tmp_lst;

def main():
    print("Request %s" % (link))
    rsps = get_rsps(me, link, enc)
    print("Request OK")
    ele_cont = parse_html_element(rsps, 'td', ['class=bg-fleet', ])
    ft_lst = parse_dygang_film_type(ele_cont)
    pretbl = PrettyTable(['编号', '名字', '链接'])
    for i in ft_lst:
        pretbl.add_row([i['id'], i['name'], i['link']])
    print(pretbl)


if __name__ == '__main__':
    main()
