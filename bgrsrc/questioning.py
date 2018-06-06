# coding: utf-8
from selenium.common.exceptions import NoSuchElementException
from src.bgrsrc import justwait


def question(window):
    try:
        justwait.justWait(window, 2)
        window.find_element_by_xpath('/html/body/div/div/div[4]/div/div[1]/button').click()
    except NoSuchElementException:
        pass
    try:
        window.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div/div[2]/div[3]/textarea').send_keys('お題募集')
    except NoSuchElementException:
        window.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div/div[1]/button/span').click()
    try:
        window.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div/div[3]/button[2]').click()
    except NoSuchElementException:
        window.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div/div/div[1]/button/span').click()
    else:
        justwait.justWait(window, 3)
