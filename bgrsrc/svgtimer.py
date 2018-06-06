# coding: utf-8
import logging

from selenium.common.exceptions import NoSuchElementException, TimeoutException

from src.bgrsrc import justwait

def svgtimerevent(window):
    """
    svgタグが存在する限りループさせます
    """
    while True:
        try:
            justwait.justWait(window, 2)
            window.find_element_by_tag_name("svg")
        except NoSuchElementException:
            break
        except TimeoutException:
            break
        else:
            justwait.justWait(window, 3)
            continue
