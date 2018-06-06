# coding: utf-8
from selenium.common.exceptions import NoSuchElementException
from bgrsrc import phase
from bgrsrc import justwait
from bgrsrc import closepriority
from bgrsrc import questioning


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