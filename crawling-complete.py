#!/usr/bin/env python
# coding: utf-8

import os
import requests

from lxml import html
from urllib.request import urlretrieve

def extracting(page_url=None):
    base = 'https://ocw.mit.edu'
    path = os.getcwd()
    page = requests.get(page_url)
    page_content = html.fromstring(page.content)
    href_url = page_content.xpath('//a/@href')   # extracting all url
    
    denominator = page_url.split('/')[-1]
    
    if not os.path.exists(path+'/temp'):
        os.mkdir('temp')
    path = path + '/temp/'
    
    print(f'strat extracting :{denominator}')
    
    for each in href_url:
        if denominator in each:
            v_url = each
            lecture = requests.get(base + v_url)
            lecture_c = html.fromstring(lecture.content)
            lecture_url = lecture_c.xpath('//a/@href')

            # extracting all pdf
            for l_url in lecture_url:

                if ('.pdf' in l_url) and ('MIT' in l_url):
                    dir_name = l_url.split('/')[-2]  # session name
                    pdf_name = l_url.split('/')[-1] # pdf_name
                    
                    PATH = (path+dir_name)
                    
                    if not os.path.exists(PATH):
                        os.mkdir(PATH)
                    
                    pdf_url = base + l_url
                    PATH = path + dir_name +'/' + pdf_name
                    urlretrieve(pdf_url, PATH)
    print(f'end extracting :{denominator}')

if __name__=='__main__':
    page_list = ['https://ocw.mit.edu/courses/mathematics/18-02sc-multivariable-calculus-fall-2010/1.-vectors-and-matrices',
        'https://ocw.mit.edu/courses/mathematics/18-02sc-multivariable-calculus-fall-2010/2.-partial-derivatives',
        'https://ocw.mit.edu/courses/mathematics/18-02sc-multivariable-calculus-fall-2010/3.-double-integrals-and-line-integrals-in-the-plane',
        'https://ocw.mit.edu/courses/mathematics/18-02sc-multivariable-calculus-fall-2010/4.-triple-integrals-and-surface-integrals-in-3-space']
    for page in page_list:
        extracting(page)
        
    print("Done with crawling")