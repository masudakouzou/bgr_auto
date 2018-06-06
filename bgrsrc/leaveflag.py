# coding: utf-8

from bgrsrc import justwait


def flag(window):
    justwait.justWait(window, 1)
    f = window.find_element_by_xpath('/html/body/div/div/div[4]/div/h3/pre').text
    if f == 'おわり' or f == '終わり':
        return True
    else:
        return False
