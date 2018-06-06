# coding: utf-8


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException


def justWait(window, timer):
    """
    処理を遅らせたいときに使う関数です
    parameters => webdriver, timer(秒)
    """
    try:
        wait = WebDriverWait(window, timer)
        wait.until(ec.presence_of_element_located((By.TAG_NAME, 'BIGIRICHAN')))
    except NoSuchElementException:
        pass
    except TimeoutException:
        pass
    else:
        pass
