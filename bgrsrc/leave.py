# coding: utf-8

from selenium.common.exceptions import NoSuchElementException
from bgrsrc import justwait


def leave(window):
    try:
        justwait.justWait(window, 5)
        window.find_element_by_xpath('/html/body/div/nav/ul/li[4]/a').click()
    except NoSuchElementException:
        return None
    else:
        justwait.justWait(window, 3)
