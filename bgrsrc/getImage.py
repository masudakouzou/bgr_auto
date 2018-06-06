# coding: utf-8
import urllib.request
import datetime
from selenium.common.exceptions import NoSuchElementException


def getSS(window):
    try:
        window.find_element_by_tag_name('img')
    except NoSuchElementException:
        pass
    else:
        png_name = datetime.datetime.now().isoformat().replace('-', '_').replace(':', '_').replace('.', '_') + '.png'
        window.save_screenshot(png_name)


def getImage(window):
    try:
        a = window.find_element_by_tag_name('img')
    except NoSuchElementException:
        pass
    else:
        png = a.screenshot_as_png
        file_name = datetime.datetime.now().isoformat().replace('-', '_').replace(':', '_').replace('.', '_') + '.png'
        with open(file_name, mode='wb') as f:
            f.write(png)
