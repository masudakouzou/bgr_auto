# coding: utf-8

from selenium.common.exceptions import NoSuchElementException
from src.bgrsrc import justwait
#   import config


def enter(window):
    try:
        justwait.justWait(window, 5)
        window.find_element_by_xpath('/html/body/div/div[2]/div/span/div[1]/div/div/div[1]/div/div[5]/div[2]/button').click()
    except NoSuchElementException:
        return None
    # PWがあるとき入力
    # else:
    #     justwait.justWait(window, 3)
    #     window.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div/input').send_keys(config.PASSWD)
    #     justwait.justWait(window, 1)
    #     window.find_element_by_xpath('/html/body/div/div/div/div/div[3]/button[2]').click()
