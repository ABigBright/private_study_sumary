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

def parse_html_element(rsps=None, selector=None):
    bs = BeautifulSoup(rsps.text, "html.parser")
    tmp_slct = bs.select(selector)
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

def parse_dygang_film_ticket(elemt_cont=None):
    tmp_dict = {'id':'', 'name':'', 'link':''}
    tmp_list = []
    for i,j in enumerate(elemt_cont):
        t1 = re.findall('<a class="classlinkclass" href="(.*)" target=.*>(.*)</a>', str(j))[0]
        tmp_dict['id'] = i
        tmp_dict['name'] = t1[1]
        tmp_dict['link'] = t1[0]
        tmp_list.append(tmp_dict.copy())
    return tmp_list

def parse_dygang_film_dldlink(elemt_cont=None):
    tmp_dict = {'id':'', 'dldlnk_type':'', 'link':''}
    tmp_list = []
    for i, j in enumerate(elemt_cont):
        r = re.findall('<a href="(.*)">(.*)</a>', str(j))[0]
        tmp_dict['id'] = i
        tmp_dict['dldlnk_type'] = r[1]
        tmp_dict['link'] = r[0]
        tmp_list.append(tmp_dict.copy())
    return tmp_list


def main():
    rsps = get_rsps(me, link, enc)
    ele_cont = parse_html_element(rsps, 'td[class="bg-fleet"] > a')
    ftype_lst = parse_dygang_film_type(ele_cont)

    for j in ftype_lst:
        rsps = get_rsps(me, j['link'], enc)
        ele_cont = parse_html_element(rsps, '.classlinkclass')
        fticket_lst = parse_dygang_film_ticket(ele_cont)
        for i in fticket_lst:
            i['film_type'] = j['name']

            rsps = get_rsps(me, i['link'], enc)
            ele_cont = parse_html_element(rsps, 'td[style="word-break: break-all; line-height: 18px"] a')
            fdldlnk_list = parse_dygang_film_dldlink(ele_cont)

            pt = PrettyTable(['编号', '链接类型', '链接', '类别'])
            for k in fdldlnk_list:
                k['film_type'] = i['film_type']
                pt.add_row([k['id'], k['dldlnk_type'], k['link'], k['film_type']])
            print(pt)

if __name__ == '__main__':
    main()
