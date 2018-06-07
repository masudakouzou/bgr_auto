# coding: utf-8

from selenium.common.exceptions import NoSuchElementException
from bgrsrc import justwait
#   import config


def enter(window):
    try:
        justwait.justWait(window, 5)
        window.find_element_by_xpath('/html/body/div/div[2]/div/span/div[1]/div/div/div[1]/div/div[5]/div[2]/button').click()
    except NoSuchElementException:
        return None
