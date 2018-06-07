# coding: utf-8
from bgrsrc import justwait
from selenium.common.exceptions import NoSuchElementException

def permission(window):
    def __find_css_selector(selector):
        try:
            window.find_element_by_css_selector(selector)
        except NoSuchElementException:
            return False
        else:
            return True

    def __wrapper_find_css_element(selector):
        try:
            ele = window.find_element_by_css_selector(selector)
        except NoSuchElementException:
            pass
        except:
            pass
        else:
            return ele

    def __wrapper_find_css_elements(selector):
        try:
            ele_list = window.find_elements_by_css_selector(selector)
        except NoSuchElementException:
            pass
        except:
            pass
        else:
            return ele_list

    def __wrapper_find_tag_element(selector):
        try:
            ele = window.find_element_by_tag_name(selector)
        except NoSuchElementException:
            pass
        except:
            pass
        else:
            return ele

    try:
        justwait.justWait(window, 2)
        window.find_element_by_xpath('/html/body/div/div/button').click()
    except NoSuchElementException:
        pass
    else:
        justwait.justWait(window, 1)

    try:
        allow_buttons = window.find_elements_by_css_selector('body > div > div.modal > div > div > div.modal-body > div > div > div > div.card-footer > div > button:nth-child(3)')
    except:
        pass
    else:
        for allow in allow_buttons:
            if '追加' in allow.text:
                justwait.justWait(window, 1)
                allow.click()

        justwait.justWait(window, 1)

    try:
        window.find_element_by_xpath('/html/body/div/div[1]/div/div/div[1]/button/span').click()
    except NoSuchElementException:
        pass
    else:
        justwait.justWait(window, 1)
