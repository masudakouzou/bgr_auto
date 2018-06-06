# coding: utf-8
from selenium.common.exceptions import NoSuchElementException
from src.bgrsrc import phase
from src.bgrsrc import justwait
from src.bgrsrc import closepriority
from src.bgrsrc import questioning


def result(window):
    while True:
        justwait.justWait(window, 5)
        a = phase.getPhaseName(window)
        if a != '結果フェーズ':
            break
        else:
            try:
                window.find_element_by_tag_name('svg')
            except NoSuchElementException:
                closepriority.close(window)
                questioning.question(window)
                break
            else:
                continue