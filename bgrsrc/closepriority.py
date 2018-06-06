# coding: utf-8
from selenium.common.exceptions import NoSuchElementException
from bgrsrc import justwait

def close(window):
    try:
        justwait.justWait(window, 1)
        window.find_element_by_xpath('/html/body/div/div/div[4]/div/div[1]/span[2]/button').click()
    except NoSuchElementException:
        return None
    else:
        justwait.justWait(window, 1)
    try:
        window.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div/div[3]/button[2]').click()
    except NoSuchElementException:
        return None
    else:
        justwait.justWait(window, 1)
