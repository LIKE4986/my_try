from time import sleep
from selenium import webdriver
import re
import requests

for i in range(2013, 2016):
    s = []
    with open('%s.txt'%i) as f:
        for i in f:
            k = i.split('`')
            print(k[2])

            browser = webdriver.Chrome()
            url = 'http://search.mtime.com/search/?q=%E9%92%A2%E9%93%81%E4%BE%A03'
            browser.get(url)
            # content = browser.page_source
            # print(content)
            content = browser.execute_script("return document.documentElement.outerHTML")
            # print(content)
            browser.close()

            data = k[2]
            link1 = '.*target="_blank" href="(.*?)"><img alt="%s' % data
            number = re.findall(link1, content)
            print(number)
            html = str(number[0]) + 'details.html'
            print(html)


            def get_page():
                url2 = requests.get(html)
                url2 = url2.text
                # print(url2)

                link2 = ' <li>.*?&nbsp;&nbsp;<a href=.*? target="_blank">(.*?)</a> '
                name = re.findall(link2, url2)
                print(name)


if __name__ == '__main__':
    get_page()
