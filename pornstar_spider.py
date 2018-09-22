#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Name:         pornstar_spider
Copyright:    snow
Version:      1.0
Email:        snowi@protonmail.com
'''

from requests_html import HTMLSession

def get_img(base_url, page):
    for p in range(page):
        session = HTMLSession()
        url = base_url + str(p)
        r = session.get(url)
        actresses = r.html.find('#waterfall', first=True)
        img_list = [ele.attrs['src'] for ele in actresses.find('img')]
        name_list = actresses.text.split('\n')
        for name, img_url in zip(name_list, img_list):
            file_name = name + '.jpg'
            r_img = session.get(img_url)
            with open(file_name, 'wb') as f:
                f.write(r_img.content)
                print(name, 'downloaded!')

if __name__ == '__main__':
    '''
    choice = input('输入序号：\n'
                   '1.日本有码女优\n'
                   '2.日本无码女优\n'
                   '3.欧美女优\n')'''
    base_url = 'https://avmoo.pw/cn/actresses/page/'
    page = 206    #可在该网站查看总页数，目前是206
    get_img(base_url, page)

    
