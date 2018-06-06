# coding: utf-8
import logging

from selenium.common.exceptions import NoSuchElementException, TimeoutException


logger = logging.getLogger(__name__)


def csvDL(window):
    try:
        logger.debug('CSV file will be Download as soon...')
        window.find_element_by_xpath('/html/body/div/nav/ul/li[3]/a').click()
    except NoSuchElementException:
        logger.warning('ダウンロードのためのボタンが見つからなかった')
    except TimeoutException:
        logger.warning('ダウンロードできなかった')
